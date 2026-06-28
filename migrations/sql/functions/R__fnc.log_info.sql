-- DROP FUNCTION fnc.log_info(text, text);

CREATE OR REPLACE FUNCTION fnc.log_info(p_source text, p_message text)
 RETURNS void
 LANGUAGE plpgsql
AS $function$
BEGIN
	perform fnc.write('INFO', p_source, p_message);
END;
$function$
;
