import pandapower.networks as nw
from sqlalchemy import create_engine, inspect, text

def export_network_to_tables(net, engine):
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    
    # Deleting 'source_' tables
    with engine.connect() as conn:
        for table in existing_tables:
            if table.startswith("source_"):
                conn.execute(text(f'DROP TABLE IF EXISTS "{table}" CASCADE'))
                print(f"Deleted table: {table}")
        conn.commit()

    # Table export
    for element, df in net.items():
        if hasattr(df, "to_sql") and not df.empty:
            table_name = f"source_{element}"
            
            # Upisivanje u bazu
            df.to_sql(table_name, engine, if_exists='replace', index_label='id')
            print(f"Export: {table_name} ({len(df)} rows)")

# Format: postgresql://username:password@host:port/database_name
engine = create_engine('postgresql://postgres:123456@localhost:5432/distrom')

# Select the Specific Network
print("Loading Network...")
net = nw.create_cigre_network_mv()

# Push to Database
print("Exporting to Database...")

export_network_to_tables(net, engine)

print("Export complete!")