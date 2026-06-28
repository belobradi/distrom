-- DROP FUNCTION fnc.log_error(text, text);

CREATE OR REPLACE FUNCTION fnc.log_error(p_source text, p_message text)
 RETURNS void
 LANGUAGE plpgsql
AS $function$
BEGIN
	perform fnc.write('ERROR', p_source, p_message);
END;
$function$
;
