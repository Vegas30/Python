PGDMP  ,                    }            warehouse_db    17.3    17.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    24811    warehouse_db    DATABASE     r   CREATE DATABASE warehouse_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru-RU';
    DROP DATABASE warehouse_db;
                     postgres    false            �            1259    24898    order_items    TABLE     J  CREATE TABLE public.order_items (
    order_item_id integer NOT NULL,
    order_id integer,
    product_id integer,
    quantity integer NOT NULL,
    unit_price numeric NOT NULL,
    total_price numeric NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT order_items_quantity_check CHECK ((quantity > 0)),
    CONSTRAINT order_items_total_price_check CHECK ((total_price > (0)::numeric)),
    CONSTRAINT order_items_unit_price_check CHECK ((unit_price > (0)::numeric))
);
    DROP TABLE public.order_items;
       public         heap r       postgres    false            �            1259    24882    orders    TABLE       CREATE TABLE public.orders (
    order_id integer NOT NULL,
    order_date date NOT NULL,
    supplier_id integer,
    total_amount numeric NOT NULL,
    status text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT orders_status_check CHECK ((status = ANY (ARRAY['в обработке'::text, 'доставлен'::text, 'отменен'::text]))),
    CONSTRAINT orders_total_amount_check CHECK ((total_amount > (0)::numeric))
);
    DROP TABLE public.orders;
       public         heap r       postgres    false            �            1259    24832    products    TABLE     �  CREATE TABLE public.products (
    product_id integer NOT NULL,
    product_name text NOT NULL,
    product_description text,
    category text,
    unit_price numeric NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT products_category_check CHECK ((category = ANY (ARRAY['электроника'::text, 'одежда'::text, 'обувь'::text, 'мебель'::text, 'товары для спорта'::text, 'инструменты'::text]))),
    CONSTRAINT products_unit_price_check CHECK ((unit_price > (0)::numeric))
);
    DROP TABLE public.products;
       public         heap r       postgres    false            �            1259    24864    stock    TABLE     p  CREATE TABLE public.stock (
    stock_id integer NOT NULL,
    product_id integer,
    warehouse_id integer,
    quantity integer NOT NULL,
    last_restocked date,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT stock_quantity_check CHECK ((quantity >= 0))
);
    DROP TABLE public.stock;
       public         heap r       postgres    false            �            1259    24853 	   suppliers    TABLE     �  CREATE TABLE public.suppliers (
    supplier_id integer NOT NULL,
    supplier_name text NOT NULL,
    contact_person text,
    phone_number text,
    email text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT suppliers_email_check CHECK ((email ~ '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'::text)),
    CONSTRAINT suppliers_phone_number_check CHECK ((phone_number ~ '^\d{10}$'::text))
);
    DROP TABLE public.suppliers;
       public         heap r       postgres    false            �            1259    24843 
   warehouses    TABLE     p  CREATE TABLE public.warehouses (
    warehouse_id integer NOT NULL,
    warehouse_name text NOT NULL,
    location text NOT NULL,
    capacity integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT warehouses_capacity_check CHECK ((capacity > 0))
);
    DROP TABLE public.warehouses;
       public         heap r       postgres    false            �          0    24898    order_items 
   TABLE DATA           �   COPY public.order_items (order_item_id, order_id, product_id, quantity, unit_price, total_price, created_at, updated_at) FROM stdin;
    public               postgres    false    222   
)       �          0    24882    orders 
   TABLE DATA           q   COPY public.orders (order_id, order_date, supplier_id, total_amount, status, created_at, updated_at) FROM stdin;
    public               postgres    false    221   ')       �          0    24832    products 
   TABLE DATA              COPY public.products (product_id, product_name, product_description, category, unit_price, created_at, updated_at) FROM stdin;
    public               postgres    false    217   D)       �          0    24864    stock 
   TABLE DATA           u   COPY public.stock (stock_id, product_id, warehouse_id, quantity, last_restocked, created_at, updated_at) FROM stdin;
    public               postgres    false    220   a)       �          0    24853 	   suppliers 
   TABLE DATA           |   COPY public.suppliers (supplier_id, supplier_name, contact_person, phone_number, email, created_at, updated_at) FROM stdin;
    public               postgres    false    219   ~)       �          0    24843 
   warehouses 
   TABLE DATA           n   COPY public.warehouses (warehouse_id, warehouse_name, location, capacity, created_at, updated_at) FROM stdin;
    public               postgres    false    218   �)       V           2606    24909    order_items order_items_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (order_item_id);
 F   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_pkey;
       public                 postgres    false    222            T           2606    24892    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public                 postgres    false    221            L           2606    24842    products products_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public                 postgres    false    217            R           2606    24871    stock stock_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_pkey PRIMARY KEY (stock_id);
 :   ALTER TABLE ONLY public.stock DROP CONSTRAINT stock_pkey;
       public                 postgres    false    220            P           2606    24863    suppliers suppliers_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.suppliers
    ADD CONSTRAINT suppliers_pkey PRIMARY KEY (supplier_id);
 B   ALTER TABLE ONLY public.suppliers DROP CONSTRAINT suppliers_pkey;
       public                 postgres    false    219            N           2606    24852    warehouses warehouses_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.warehouses
    ADD CONSTRAINT warehouses_pkey PRIMARY KEY (warehouse_id);
 D   ALTER TABLE ONLY public.warehouses DROP CONSTRAINT warehouses_pkey;
       public                 postgres    false    218            Z           2606    24910 %   order_items order_items_order_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(order_id) ON DELETE CASCADE;
 O   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_order_id_fkey;
       public               postgres    false    4692    222    221            [           2606    24915 '   order_items order_items_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE CASCADE;
 Q   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_product_id_fkey;
       public               postgres    false    4684    217    222            Y           2606    24893    orders orders_supplier_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_supplier_id_fkey FOREIGN KEY (supplier_id) REFERENCES public.suppliers(supplier_id) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_supplier_id_fkey;
       public               postgres    false    221    219    4688            W           2606    24872    stock stock_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.stock DROP CONSTRAINT stock_product_id_fkey;
       public               postgres    false    220    217    4684            X           2606    24877    stock stock_warehouse_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_warehouse_id_fkey FOREIGN KEY (warehouse_id) REFERENCES public.warehouses(warehouse_id) ON DELETE CASCADE;
 G   ALTER TABLE ONLY public.stock DROP CONSTRAINT stock_warehouse_id_fkey;
       public               postgres    false    4686    218    220            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     