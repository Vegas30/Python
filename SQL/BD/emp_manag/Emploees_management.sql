PGDMP                      }            Emploees_management    17.3    17.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16388    Emploees_management    DATABASE     {   CREATE DATABASE "Emploees_management" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru-RU';
 %   DROP DATABASE "Emploees_management";
                     postgres    false            �            1259    24743    departments    TABLE     �   CREATE TABLE public.departments (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    created_at date DEFAULT CURRENT_DATE
);
    DROP TABLE public.departments;
       public         heap r       postgres    false            �            1259    24742    departments_id_seq    SEQUENCE     �   CREATE SEQUENCE public.departments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.departments_id_seq;
       public               postgres    false    218            �           0    0    departments_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.departments_id_seq OWNED BY public.departments.id;
          public               postgres    false    217            �            1259    24751 	   employees    TABLE     �   CREATE TABLE public.employees (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    phone character varying(20),
    department_id integer,
    hired_at date DEFAULT CURRENT_DATE
);
    DROP TABLE public.employees;
       public         heap r       postgres    false            �            1259    24750    employees_id_seq    SEQUENCE     �   CREATE SEQUENCE public.employees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.employees_id_seq;
       public               postgres    false    220            �           0    0    employees_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.employees_id_seq OWNED BY public.employees.id;
          public               postgres    false    219            �            1259    24768    tasks    TABLE     %  CREATE TABLE public.tasks (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    description text,
    status character varying(50) DEFAULT 'Создана'::character varying,
    assigned_to integer,
    created_at date DEFAULT CURRENT_DATE,
    due_date date,
    CONSTRAINT tasks_check CHECK ((due_date >= created_at)),
    CONSTRAINT tasks_status_check CHECK (((status)::text = ANY ((ARRAY['Создана'::character varying, 'В процессе'::character varying, 'Завершена'::character varying])::text[])))
);
    DROP TABLE public.tasks;
       public         heap r       postgres    false            �            1259    24767    tasks_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.tasks_id_seq;
       public               postgres    false    222            �           0    0    tasks_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;
          public               postgres    false    221            +           2604    24746    departments id    DEFAULT     p   ALTER TABLE ONLY public.departments ALTER COLUMN id SET DEFAULT nextval('public.departments_id_seq'::regclass);
 =   ALTER TABLE public.departments ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    217    218    218            -           2604    24754    employees id    DEFAULT     l   ALTER TABLE ONLY public.employees ALTER COLUMN id SET DEFAULT nextval('public.employees_id_seq'::regclass);
 ;   ALTER TABLE public.employees ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    220    219    220            /           2604    24771    tasks id    DEFAULT     d   ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);
 7   ALTER TABLE public.tasks ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    221    222    222            �          0    24743    departments 
   TABLE DATA           ;   COPY public.departments (id, name, created_at) FROM stdin;
    public               postgres    false    218   �        �          0    24751 	   employees 
   TABLE DATA           T   COPY public.employees (id, name, email, phone, department_id, hired_at) FROM stdin;
    public               postgres    false    220   3"       �          0    24768    tasks 
   TABLE DATA           b   COPY public.tasks (id, title, description, status, assigned_to, created_at, due_date) FROM stdin;
    public               postgres    false    222   �$       �           0    0    departments_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.departments_id_seq', 19, true);
          public               postgres    false    217            �           0    0    employees_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.employees_id_seq', 66, true);
          public               postgres    false    219            �           0    0    tasks_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.tasks_id_seq', 42, true);
          public               postgres    false    221            5           2606    24749    departments departments_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_pkey;
       public                 postgres    false    218            7           2606    24761    employees employees_email_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_email_key UNIQUE (email);
 G   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_email_key;
       public                 postgres    false    220            9           2606    24759    employees employees_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_pkey;
       public                 postgres    false    220            ;           2606    24779    tasks tasks_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.tasks DROP CONSTRAINT tasks_pkey;
       public                 postgres    false    222            <           2606    24762 &   employees employees_department_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(id) ON UPDATE CASCADE ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_department_id_fkey;
       public               postgres    false    218    4661    220            =           2606    24780    tasks tasks_assigned_to_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_assigned_to_fkey FOREIGN KEY (assigned_to) REFERENCES public.employees(id);
 F   ALTER TABLE ONLY public.tasks DROP CONSTRAINT tasks_assigned_to_fkey;
       public               postgres    false    222    4665    220            �   ^  x�]RKR�0[ۧ�`�|J{֬9L���,X0���~ܤM� �=Sl�LI�$Kz6
ϰ~�-����K�gyq�>:Wx�EM��1[؄�t��/��t��t,�~�iV�J�JV����Y����c�p�wX�?;�r�s��Р&�J�L�-�*=Px�lI�8�J�s�8Txg�yD�I�M�p��w!B�K� �`�)6N���5_��I��ؑ*P�#��k~v��В[��H�-a�9
�a
��C�u�.�ư��1͏�����Bիu���"D�d��,�{M�|���x}Y�#��ɻ�/�w��>��b�}Qz -�hi�xe�<�ܝ���y�ػ<�Z�$Js      �   �  x����j�0���Sh_,��e��F$njƗ0�d����RZ(��C.0�$y����63	I�����sx�|7�fax�0�撥Ǻ�;�u���9��UF����T;�ܑ�Ͻ����(K,�U�����0���q~�d揹����s�T�mL�<P>�$.�F9(�Y��e����;���4��,�T+�!�z�p���fen�]}n˺&q�#+Sg��H�+8L�`�h�(f�Y΃Y�~��L���,)��>S=K�N��/��U���olo �H'e�O��a�(B1w]�LIi���Cg�
 ��f��0�<���ɀ�N99�R��zN�&����#�Q�.��ҳqRA����E=I��|5��R�,I���$�i5I�m�.��x@��]�����e��Q�DW�4��DF��F��~�	L���5P$ݵu`{�8�i��Ơ1�܆/Lt�D}�I]AJ Z�׶�Յ�t���B\؂�mVH��薍ev�B�
����>M�� UK����"��<�����|�	�3�U��EW��Z���(����E�Lt3�[1X? �iQ��)r�ԡU;)tnQ��{os�D8|&��X���k����8ݯ�'��Q��X`g�����v�V�����V��Bc����D��vV�k�jP��!�׻������      �   �  x��VY��@��O���8����$���@�f��I�'��+T߈W�^����O��]K��j�-�I�ZОbuM	����6x�v�2�#��R��}��I�ԒϪk����s��4ǋ��6�u�n��H�h�E��w��lZ�������<7��Y��Qw�Z�[�ݳ�{�AF���=�L��̾�=ŒҨJ)�}<ڞE�px!=P{	s��$԰�R}j�Y�n��)�E�Fml�?a	��e��;�P��إ�X�9k‭��f�,��`��<o�VxXRl�K�܂UN�
ʘ�G&����O���VQXB5�&}���4�5�:�X�-w�6��K�ܤR�[��Ԣr�D��r;f����y����C�X�Z��u;5���1c�qQ�RX=04��*h�ϓct������N��N"t�Dz ��\6��-�����K �,`�"/rЦy^�f(}��n,/_]M_LGu�\3i\�Md%xq"I"�~X�0�c'�gH��1P%>�w��bl�+f�c�?)�*�����mA/|�RW�.��h�[9r<��G%�K�d�V���.x���[����yp�F�h���-�FR'���e�Ō���ly]7}����ɪi��������K�k��)>qT`���4��f{�=:��Z9$��0�*�Ib��혵t�򃀆���g@��&U���.)�/B[HO��"��F]�M�^U5�hj,\հ��B��g�2��v���!�R@��Y�X�쵶or�152��_���䍦�E]�!�����17-|�l��d�9
��M^�$��w��f@�4��&s��Scq.8�s������mOw��|�ĭM���=����G��*K��˃���2�_��m�?K���     