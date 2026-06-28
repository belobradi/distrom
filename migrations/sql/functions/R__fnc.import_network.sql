-- DROP FUNCTION fnc.import_network(text, text);

CREATE OR REPLACE FUNCTION fnc.import_network()
 RETURNS void
 LANGUAGE plpgsql
AS $function$
DECLARE
    tbl text;
BEGIN
    FOREACH tbl IN ARRAY ARRAY[
        'bus'
       ,'ext_grid'
       ,'line'
       ,'load'
       ,'sgen'
       ,'switch'
       ,'trafo'
    ]
    LOOP
        EXECUTE format('TRUNCATE TABLE public.param_%I', tbl);

        EXECUTE format(
            'INSERT INTO "public"."param_%I"
             SELECT * FROM "source"."%I"',
            tbl, tbl
        );
    END LOOP;
END;
$function$
;