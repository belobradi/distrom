-- DROP FUNCTION fnc.write_log(text, text, text);

CREATE OR REPLACE FUNCTION fnc.write_log(p_level text, p_source text, p_message text)
 RETURNS void
 LANGUAGE plpgsql
AS $function$
BEGIN
    INSERT INTO public.execution_logs(
        "timestamp",
        level,
        function,
        message
    )
    VALUES (
        now(),
        p_level,
        p_source,
        p_message
    );
END;
$function$
;
