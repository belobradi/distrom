import pandapower.networks as nw
from sqlalchemy import text
import src.common.Logging as Logging
from src.common.db_utils import get_db_connection

def export_network_to_tables(net, engine):
    schema = 'source'
    Logging.log_info(engine, f"Exporting to '{schema}' schema...")

    for element, df in net.items():
        if hasattr(df, "to_sql") and not df.empty:
            df.to_sql(element, engine, schema=schema, if_exists='replace', index_label='id')
            Logging.log_info(engine, f"Export: {element} ({len(df)} rows)")

    Logging.log_info(engine, "Export complete!")

def main():
    engine = get_db_connection()
    Logging.log_info(engine, "Loading mv_oberrhein Network...")
    net = nw.mv_oberrhein()
    export_network_to_tables(net, engine)

if __name__ == "__main__":
    main()