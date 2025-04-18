PGDMP  '                    }            task_manager    17.3    17.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    24785    task_manager    DATABASE     r   CREATE DATABASE task_manager WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru-RU';
    DROP DATABASE task_manager;
                     postgres    false            �            1259    24787 
   categories    TABLE     T   CREATE TABLE public.categories (
    id integer NOT NULL,
    name text NOT NULL
);
    DROP TABLE public.categories;
       public         heap r       postgres    false            �            1259    24786    categories_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.categories_id_seq;
       public               postgres    false    218            �           0    0    categories_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;
          public               postgres    false    217            �            1259    24796    tasks    TABLE     �   CREATE TABLE public.tasks (
    id integer NOT NULL,
    task_text text NOT NULL,
    category_id integer,
    status text DEFAULT 'В процессе'::text,
    priority text DEFAULT 'Средний'::text
);
    DROP TABLE public.tasks;
       public         heap r       postgres    false            �            1259    24795    tasks_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.tasks_id_seq;
       public               postgres    false    220            �           0    0    tasks_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;
          public               postgres    false    219            &           2604    24790    categories id    DEFAULT     n   ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);
 <   ALTER TABLE public.categories ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    217    218    218            '           2604    24799    tasks id    DEFAULT     d   ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);
 7   ALTER TABLE public.tasks ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    220    219    220            �          0    24787 
   categories 
   TABLE DATA           .   COPY public.categories (id, name) FROM stdin;
    public               postgres    false    218   �       �          0    24796    tasks 
   TABLE DATA           M   COPY public.tasks (id, task_text, category_id, status, priority) FROM stdin;
    public               postgres    false    220          �           0    0    categories_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.categories_id_seq', 3, true);
          public               postgres    false    217            �           0    0    tasks_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.tasks_id_seq', 6, true);
          public               postgres    false    219            +           2606    24794    categories categories_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public                 postgres    false    218            -           2606    24805    tasks tasks_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.tasks DROP CONSTRAINT tasks_pkey;
       public                 postgres    false    220            .           2606    24806    tasks tasks_category_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id) ON DELETE SET NULL;
 F   ALTER TABLE ONLY public.tasks DROP CONSTRAINT tasks_category_id_fkey;
       public               postgres    false    218    4651    220            �   9   x�3估�/��ta����/l
l�2�0�� w�}�r��qqq �<�      �   Z   x�3�0�¾[.l���b����M{@܋��^l���0I����@�6�P���[�b���}v]�qa'�1&cP� 7�_\     