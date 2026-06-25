DROP VIEW IF EXISTS public.execution_logs_v;
CREATE OR REPLACE VIEW public.execution_logs_v
AS SELECT
    "timestamp",
    function,
    level,
    message
FROM public.execution_logs 
ORDER BY "timestamp" DESC;