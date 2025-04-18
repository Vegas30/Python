PGDMP                      }         	   Python-41    17.2    17.2 #    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16387 	   Python-41    DATABASE        CREATE DATABASE "Python-41" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "Python-41";
                     postgres    false                        2615    16388    schema_name    SCHEMA        CREATE SCHEMA schema_name;
    DROP SCHEMA schema_name;
                     postgres    false            �            1255    16448 Y   calculate_amount_total(integer, timestamp without time zone, timestamp without time zone)    FUNCTION     x  CREATE FUNCTION public.calculate_amount_total(cl_id integer, start_date timestamp without time zone, end_date timestamp without time zone) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE
	total DECIMAL(10,2);
BEGIN
	SELECT SUM(amount) INTO total
	FROM transactions
	WHERE client_id = cl_id	AND transaction_date BETWEEN start_date AND end_date;

	RETURN total;
END;
$$;
 �   DROP FUNCTION public.calculate_amount_total(cl_id integer, start_date timestamp without time zone, end_date timestamp without time zone);
       public               postgres    false            �            1259    16436    clients    TABLE     ,  CREATE TABLE public.clients (
    id integer NOT NULL,
    name character varying(25) NOT NULL,
    type character varying(50),
    contact_info jsonb,
    CONSTRAINT clients_type_check CHECK (((type)::text = ANY ((ARRAY['individual'::character varying, 'business'::character varying])::text[])))
);
    DROP TABLE public.clients;
       public         heap r       postgres    false            �            1259    16435    clients_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.clients_id_seq;
       public               postgres    false    225            �           0    0    clients_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.clients_id_seq OWNED BY public.clients.id;
          public               postgres    false    224            �            1259    16427 	   employees    TABLE     �   CREATE TABLE public.employees (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    role character varying(255),
    contact_info jsonb
);
    DROP TABLE public.employees;
       public         heap r       postgres    false            �            1259    16426    employees_id_seq    SEQUENCE     �   CREATE SEQUENCE public.employees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.employees_id_seq;
       public               postgres    false    223            �           0    0    employees_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.employees_id_seq OWNED BY public.employees.id;
          public               postgres    false    222            �            1259    16400    services    TABLE     �   CREATE TABLE public.services (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    category character varying(255),
    price numeric(10,2) NOT NULL
);
    DROP TABLE public.services;
       public         heap r       postgres    false            �            1259    16399    services_id_seq    SEQUENCE     �   CREATE SEQUENCE public.services_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.services_id_seq;
       public               postgres    false    219            �           0    0    services_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.services_id_seq OWNED BY public.services.id;
          public               postgres    false    218            �            1259    16409    transactions    TABLE     �   CREATE TABLE public.transactions (
    id integer NOT NULL,
    client_id integer,
    service_id integer,
    transaction_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    amount numeric(10,2) NOT NULL
);
     DROP TABLE public.transactions;
       public         heap r       postgres    false            �            1259    16408    transactions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.transactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.transactions_id_seq;
       public               postgres    false    221            �           0    0    transactions_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.transactions_id_seq OWNED BY public.transactions.id;
          public               postgres    false    220            6           2604    16439 
   clients id    DEFAULT     h   ALTER TABLE ONLY public.clients ALTER COLUMN id SET DEFAULT nextval('public.clients_id_seq'::regclass);
 9   ALTER TABLE public.clients ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    225    224    225            5           2604    16430    employees id    DEFAULT     l   ALTER TABLE ONLY public.employees ALTER COLUMN id SET DEFAULT nextval('public.employees_id_seq'::regclass);
 ;   ALTER TABLE public.employees ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    222    223    223            2           2604    16403    services id    DEFAULT     j   ALTER TABLE ONLY public.services ALTER COLUMN id SET DEFAULT nextval('public.services_id_seq'::regclass);
 :   ALTER TABLE public.services ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    219    218    219            3           2604    16412    transactions id    DEFAULT     r   ALTER TABLE ONLY public.transactions ALTER COLUMN id SET DEFAULT nextval('public.transactions_id_seq'::regclass);
 >   ALTER TABLE public.transactions ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    220    221    221            �          0    16436    clients 
   TABLE DATA           ?   COPY public.clients (id, name, type, contact_info) FROM stdin;
    public               postgres    false    225   
(       �          0    16427 	   employees 
   TABLE DATA           A   COPY public.employees (id, name, role, contact_info) FROM stdin;
    public               postgres    false    223   �)       �          0    16400    services 
   TABLE DATA           =   COPY public.services (id, name, category, price) FROM stdin;
    public               postgres    false    219   "+       �          0    16409    transactions 
   TABLE DATA           [   COPY public.transactions (id, client_id, service_id, transaction_date, amount) FROM stdin;
    public               postgres    false    221   e,       �           0    0    clients_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.clients_id_seq', 6, true);
          public               postgres    false    224            �           0    0    employees_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.employees_id_seq', 6, true);
          public               postgres    false    222            �           0    0    services_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.services_id_seq', 8, true);
          public               postgres    false    218            �           0    0    transactions_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.transactions_id_seq', 15, true);
          public               postgres    false    220            ?           2606    16444    clients clients_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.clients DROP CONSTRAINT clients_pkey;
       public                 postgres    false    225            =           2606    16434    employees employees_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_pkey;
       public                 postgres    false    223            9           2606    16407    services services_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.services DROP CONSTRAINT services_pkey;
       public                 postgres    false    219            ;           2606    16415    transactions transactions_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.transactions DROP CONSTRAINT transactions_pkey;
       public                 postgres    false    221            @           2606    16421 )   transactions transactions_service_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.services(id);
 S   ALTER TABLE ONLY public.transactions DROP CONSTRAINT transactions_service_id_fkey;
       public               postgres    false    4665    221    219            �   p  x����J�@�ד�f��%I��<��4��4�I$�\�Pp��x����%���9��mI)��9�9������f����@
3��>�X?�tJ��b�b�"��IO���Њ�Gdo�]���Z�S�Ầ�FCm�H�h�!�ư�.0<�"��G���0<*|Y� �n����jK���!?�����	�%�[y��γ)$��4�츇����:�V�7IF��bG6�i/`�h���n��> V�pY�y�~ϊD�r]�*���/LA���[T��-W��;VH
���g�b��l���0��7�-�����+֋@�vG^�z��)s'p%��d-de&�r�6w�es@y@��٥�v]ۙ�ƄX9�(��]�      �   �  x�}��J�@���S�l5�IMӸʃ%�i�fJ/���tQAD����J��p�F�3�P���3'��/1z�1�hMk4�%Mi�����H{4K��@��Y�#�T��ďyR��/b��*��kz��c&^8r47��l�6�(��+�R蕦� ���Fo�p���z�d�5-�;p���d�O�r۫�ݍ:ab�E���� 6�	m2�F�8.��t��O�#Z����s�ˉ�a��!���k�� �(� w�Cx�� S}ƶ��/D��eUY���6k%a�"�`�4��V�AV�پ0r� ���e��*�����taβ�B�b֖�oS&*z��+����z���&�B���:�T���mÎx�ku��1��L�YNU�o��I�      �   3  x�u�=N�@���)|"���+ х�E�D~$��(�j*$zd�8���+�ވyk����7ߛm_�Uϐb�T�#�>�ͣB�}�\?萗wY�C�����ӫ��?W��8=Ǳ\�g$Xq&�!��|*��%��]@�i���w�TW6�rN�x]��Pv�G�wq�)d���Ƌ�	Y���O�E��E��Ȅ"��sAI]�x5;r�0ߥ�g�/����_	ێ��
�2�n�QB�e��6��ʡ�#��`�ņ�92۔��1l��S�8 KZ��e��H��:
�-'n�gY��>4�      �   �   x�]���0D��
��%�hj���8�Co��7�<.�Qhޠ(DM��b v`U�SI�+�:O�Dj͝HHn+1��yC8��!<*odV98)BV�H��(�� N�9�)c��M� .�7�;��ժ�B�f�Y����3ݛU��g�˄9j37NMD_��rKU{�gzyan���Л<�ЄS�C�*a�]o~����~W�Yt     