-- Create the execution logs table with proper constraints
CREATE TABLE IF NOT EXISTS execution_logs (
    id SERIAL PRIMARY KEY,
    function text NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    level VARCHAR(10) NOT NULL,
    message TEXT NOT NULL
);
CREATE INDEX idx_logs_timestamp ON execution_logs(timestamp DESC);