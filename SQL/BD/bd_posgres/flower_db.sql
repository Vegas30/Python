PGDMP                        }         	   flower_db    17.2    17.2 %    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    32879 	   flower_db    DATABASE     }   CREATE DATABASE flower_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE flower_db;
                     postgres    false            �            1259    32891    clients    TABLE     �   CREATE TABLE public.clients (
    client_id integer NOT NULL,
    full_name character varying(100) NOT NULL,
    phone character varying(20),
    email character varying(100),
    registration_date date DEFAULT CURRENT_DATE
);
    DROP TABLE public.clients;
       public         heap r       postgres    false            �            1259    32890    clients_client_id_seq    SEQUENCE     �   CREATE SEQUENCE public.clients_client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.clients_client_id_seq;
       public               postgres    false    220            �           0    0    clients_client_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.clients_client_id_seq OWNED BY public.clients.client_id;
          public               postgres    false    219            �            1259    32881    flowers    TABLE     �  CREATE TABLE public.flowers (
    flower_id integer NOT NULL,
    name character varying(50) NOT NULL,
    price numeric(8,2),
    quantity integer,
    image_path character varying(255),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT flowers_price_check CHECK ((price > (0)::numeric)),
    CONSTRAINT flowers_quantity_check CHECK ((quantity >= 0))
);
    DROP TABLE public.flowers;
       public         heap r       postgres    false            �            1259    32880    flowers_flower_id_seq    SEQUENCE     �   CREATE SEQUENCE public.flowers_flower_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.flowers_flower_id_seq;
       public               postgres    false    218            �           0    0    flowers_flower_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.flowers_flower_id_seq OWNED BY public.flowers.flower_id;
          public               postgres    false    217            �            1259    32917    order_items    TABLE     �   CREATE TABLE public.order_items (
    item_id integer NOT NULL,
    order_id integer,
    flower_id integer,
    quantity integer,
    CONSTRAINT order_items_quantity_check CHECK ((quantity > 0))
);
    DROP TABLE public.order_items;
       public         heap r       postgres    false            �            1259    32916    order_items_item_id_seq    SEQUENCE     �   CREATE SEQUENCE public.order_items_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.order_items_item_id_seq;
       public               postgres    false    224            �           0    0    order_items_item_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.order_items_item_id_seq OWNED BY public.order_items.item_id;
          public               postgres    false    223            �            1259    32903    orders    TABLE     �  CREATE TABLE public.orders (
    order_id integer NOT NULL,
    client_id integer,
    status character varying(20),
    order_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT orders_status_check CHECK (((status)::text = ANY ((ARRAY['Новый'::character varying, 'В обработке'::character varying, 'Выполнен'::character varying, 'Отменен'::character varying])::text[])))
);
    DROP TABLE public.orders;
       public         heap r       postgres    false            �            1259    32902    orders_order_id_seq    SEQUENCE     �   CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.orders_order_id_seq;
       public               postgres    false    222            �           0    0    orders_order_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;
          public               postgres    false    221            2           2604    32894    clients client_id    DEFAULT     v   ALTER TABLE ONLY public.clients ALTER COLUMN client_id SET DEFAULT nextval('public.clients_client_id_seq'::regclass);
 @   ALTER TABLE public.clients ALTER COLUMN client_id DROP DEFAULT;
       public               postgres    false    220    219    220            0           2604    32884    flowers flower_id    DEFAULT     v   ALTER TABLE ONLY public.flowers ALTER COLUMN flower_id SET DEFAULT nextval('public.flowers_flower_id_seq'::regclass);
 @   ALTER TABLE public.flowers ALTER COLUMN flower_id DROP DEFAULT;
       public               postgres    false    218    217    218            6           2604    32920    order_items item_id    DEFAULT     z   ALTER TABLE ONLY public.order_items ALTER COLUMN item_id SET DEFAULT nextval('public.order_items_item_id_seq'::regclass);
 B   ALTER TABLE public.order_items ALTER COLUMN item_id DROP DEFAULT;
       public               postgres    false    223    224    224            4           2604    32906    orders order_id    DEFAULT     r   ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);
 >   ALTER TABLE public.orders ALTER COLUMN order_id DROP DEFAULT;
       public               postgres    false    222    221    222            �          0    32891    clients 
   TABLE DATA           X   COPY public.clients (client_id, full_name, phone, email, registration_date) FROM stdin;
    public               postgres    false    220   �,       �          0    32881    flowers 
   TABLE DATA           [   COPY public.flowers (flower_id, name, price, quantity, image_path, created_at) FROM stdin;
    public               postgres    false    218   W.       �          0    32917    order_items 
   TABLE DATA           M   COPY public.order_items (item_id, order_id, flower_id, quantity) FROM stdin;
    public               postgres    false    224   �/       �          0    32903    orders 
   TABLE DATA           I   COPY public.orders (order_id, client_id, status, order_date) FROM stdin;
    public               postgres    false    222   �/       �           0    0    clients_client_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.clients_client_id_seq', 10, true);
          public               postgres    false    219            �           0    0    flowers_flower_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.flowers_flower_id_seq', 10, true);
          public               postgres    false    217            �           0    0    order_items_item_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.order_items_item_id_seq', 10, true);
          public               postgres    false    223            �           0    0    orders_order_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.orders_order_id_seq', 10, true);
          public               postgres    false    221            >           2606    32901    clients clients_email_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_email_key UNIQUE (email);
 C   ALTER TABLE ONLY public.clients DROP CONSTRAINT clients_email_key;
       public                 postgres    false    220            @           2606    32899    clients clients_phone_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_phone_key UNIQUE (phone);
 C   ALTER TABLE ONLY public.clients DROP CONSTRAINT clients_phone_key;
       public                 postgres    false    220            B           2606    32897    clients clients_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (client_id);
 >   ALTER TABLE ONLY public.clients DROP CONSTRAINT clients_pkey;
       public                 postgres    false    220            <           2606    32889    flowers flowers_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.flowers
    ADD CONSTRAINT flowers_pkey PRIMARY KEY (flower_id);
 >   ALTER TABLE ONLY public.flowers DROP CONSTRAINT flowers_pkey;
       public                 postgres    false    218            F           2606    32923    order_items order_items_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (item_id);
 F   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_pkey;
       public                 postgres    false    224            D           2606    32910    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public                 postgres    false    222            H           2606    32929 &   order_items order_items_flower_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_flower_id_fkey FOREIGN KEY (flower_id) REFERENCES public.flowers(flower_id) ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_flower_id_fkey;
       public               postgres    false    218    4668    224            I           2606    32924 %   order_items order_items_order_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(order_id) ON DELETE CASCADE;
 O   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_order_id_fkey;
       public               postgres    false    222    4676    224            G           2606    32911    orders orders_client_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.clients(client_id) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_client_id_fkey;
       public               postgres    false    4674    222    220            �   i  x�u��j�@���)�/�\2�d��fh�-V��Ki�H/�'H�A��g8�F=Iju	�8���p�g�a��1�C;�-�����B�J{�L�41Q�8o' �Pu&�L���4��c���/ܖ	��L*���<HL'2�!�ט������ىv���ʕ`��2�|õ�S'�4�ٻ=����� �vܬ�(�G��e���dZ|�&]וR�H�n�_���6���ᯐO�e{K�O��V����<��y�Ʉ2Tӿ�s.��pv�a��|*�-$�EK\v"%-��qx ]��&2\;t��:�=�j՚".M/�+#8��{2�#;.1e�����W������Y�V����%7      �   B  x��ѽN�0�����@]ۉ��ga	!j�ڤrڡ �baAB��^P+"J�+\ވs�z�/���Y ���qB�,�a����l��iKv1��Rx8���F2ɐEB�QH�����=��
w�2w�|1�3>c�[�:��BGL�d�"�G����i���UDꨌKsV��)�n(e�ʑ�%�n���>�91�+{�٘�E4����M�)�3}�gM��$,���"7u>�M��R��Ng����i�_
�o�,ۼ�W�t1����5�+;�`��ȥi�[� ���UK'eY��Ҿ]S��MI>�A����^      �   >   x��� !�oO1+@/�_�Y~
oѭ���`کb٥N�Ԥli��J�=
�����A
�      �   �   x�����0��4��^�Z(q��j H9�I�¸#L����fFZ^���|B��V�V���Al�$�@�KQk�oΜ8oy��;�⛂�|�#�|��V�Ã��>��a�����IH��G_)�F�:{�R_pG�v     