import pandapower.networks as nw
from sqlalchemy import inspect, text
import src.common.Logging as Logging
from db_utils import get_db_connection

def export_network_to_tables(net, engine):
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    
    # Deleting 'source_' tables
    with engine.connect() as conn:
        for table in existing_tables:
            if table.startswith("source_"):
                conn.execute(text(f'DROP TABLE IF EXISTS "{table}" CASCADE'))
                Logging.log_debug(engine, f"Deleted table: {table}")
        conn.commit()

    # Table export
    for element, df in net.items():
        if hasattr(df, "to_sql") and not df.empty:
            table_name = f"source_{element}"
            df.to_sql(table_name, engine, if_exists='replace', index_label='id')
            Logging.log_info(engine, f"Export: {table_name} ({len(df)} rows)")

def main():
    engine = get_db_connection()

    Logging.log_info(engine, "Loading Network...")
    net = nw.create_cigre_network_mv()

    Logging.log_info(engine, "Exporting to Database...")
    export_network_to_tables(net, engine)
    Logging.log_info(engine, "Export complete!")

if __name__ == "__main__":
    main()