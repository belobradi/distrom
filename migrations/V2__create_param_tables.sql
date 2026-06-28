-- DROP TABLE public.param_bus;
CREATE TABLE public.param_bus (
	id int8 NULL,
	"name" text NULL,
	vn_kv float8 NULL,
	"type" text NULL,
	"zone" text NULL,
	in_service bool NULL,
	geo text NULL
);

-- DROP TABLE public.param_ext_grid;
CREATE TABLE public.param_ext_grid (
	id int8 NULL,
	"name" text NULL,
	bus int8 NULL,
	vm_pu float8 NULL,
	va_degree float8 NULL,
	slack_weight float8 NULL,
	in_service bool NULL,
	rx_max float8 NULL,
	rx_min float8 NULL,
	s_sc_max_mva float8 NULL,
	s_sc_min_mva float8 NULL
);

-- DROP TABLE public.param_line;
CREATE TABLE public.param_line (
	id int8 NULL,
	"name" text NULL,
	std_type text NULL,
	from_bus int8 NULL,
	to_bus int8 NULL,
	length_km float8 NULL,
	r_ohm_per_km float8 NULL,
	x_ohm_per_km float8 NULL,
	c_nf_per_km float8 NULL,
	g_us_per_km float8 NULL,
	max_i_ka float8 NULL,
	df float8 NULL,
	"parallel" int8 NULL,
	"type" text NULL,
	in_service bool NULL,
	geo text NULL
);

-- DROP TABLE public.param_load;
CREATE TABLE public.param_load (
	id int8 NULL,
	"name" text NULL,
	bus int8 NULL,
	p_mw float8 NULL,
	q_mvar float8 NULL,
	const_z_p_percent float8 NULL,
	const_z_q_percent float8 NULL,
	const_i_p_percent float8 NULL,
	const_i_q_percent float8 NULL,
	sn_mva float8 NULL,
	scaling float8 NULL,
	in_service bool NULL,
	"type" text NULL
);

-- DROP TABLE public.param_sgen;
CREATE TABLE public.param_sgen (
	id int8 NULL,
	"name" text NULL,
	bus int8 NULL,
	p_mw float8 NULL,
	q_mvar float8 NULL,
	sn_mva float8 NULL,
	scaling float8 NULL,
	in_service bool NULL,
	"type" text NULL,
	current_source bool NULL,
	id_q_capability_characteristic int8 NULL,
	reactive_capability_curve bool NULL,
	curve_style text NULL
);

-- DROP TABLE public.param_switch;
CREATE TABLE public.param_switch (
	id int8 NULL,
	bus int8 NULL,
	"element" int8 NULL,
	et text NULL,
	"type" text NULL,
	closed bool NULL,
	"name" text NULL,
	z_ohm float8 NULL,
	in_ka float8 NULL
);

-- DROP TABLE public.param_trafo;
CREATE TABLE public.param_trafo (
	id int8 NULL,
	"name" text NULL,
	std_type text NULL,
	hv_bus int8 NULL,
	lv_bus int8 NULL,
	sn_mva float8 NULL,
	vn_hv_kv float8 NULL,
	vn_lv_kv float8 NULL,
	vk_percent float8 NULL,
	vkr_percent float8 NULL,
	pfe_kw float8 NULL,
	i0_percent float8 NULL,
	shift_degree float8 NULL,
	tap_side text NULL,
	tap_neutral float8 NULL,
	tap_min float8 NULL,
	tap_max float8 NULL,
	tap_step_percent float8 NULL,
	tap_step_degree float8 NULL,
	tap_pos float8 NULL,
	"parallel" int8 NULL,
	df float8 NULL,
	in_service bool NULL,
	tap_changer_type text NULL
);