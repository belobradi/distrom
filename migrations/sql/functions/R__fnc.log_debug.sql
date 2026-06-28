-- DROP FUNCTION fnc.log_debug(text, text);

CREATE OR REPLACE FUNCTION fnc.log_debug(p_source text, p_message text)
 RETURNS void
 LANGUAGE plpgsql
AS $function$
BEGIN
	perform fnc.write('DEBUG', p_source, p_message);
END;
$function$
;