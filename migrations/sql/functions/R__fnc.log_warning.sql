-- DROP FUNCTION fnc.log_warning(text, text);

CREATE OR REPLACE FUNCTION fnc.log_warning(p_source text, p_message text)
 RETURNS void
 LANGUAGE plpgsql
AS $function$
BEGIN
	perform fnc.write('WARNING', p_source, p_message);
END;
$function$
;
