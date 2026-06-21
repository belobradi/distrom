-- Create the system logs table with proper constraints
CREATE TABLE IF NOT EXISTS system_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    level VARCHAR(10) NOT NULL,
    message TEXT NOT NULL
);
CREATE INDEX idx_logs_timestamp ON system_logs(timestamp DESC);
