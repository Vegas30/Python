PGDMP                      }            courses_manager    17.2    17.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    32833    courses_manager    DATABASE     �   CREATE DATABASE courses_manager WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE courses_manager;
                     postgres    false            �            1259    32853    courses    TABLE     }   CREATE TABLE public.courses (
    id integer NOT NULL,
    title character varying(60),
    professor_id integer NOT NULL
);
    DROP TABLE public.courses;
       public         heap r       postgres    false            �            1259    32852    courses_id_seq    SEQUENCE     �   CREATE SEQUENCE public.courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.courses_id_seq;
       public               postgres    false    222            �           0    0    courses_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;
          public               postgres    false    221            �            1259    32835 
   professors    TABLE     a   CREATE TABLE public.professors (
    id integer NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public.professors;
       public         heap r       postgres    false            �            1259    32834    professors_id_seq    SEQUENCE     �   CREATE SEQUENCE public.professors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.professors_id_seq;
       public               postgres    false    218            �           0    0    professors_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.professors_id_seq OWNED BY public.professors.id;
          public               postgres    false    217            �            1259    32844    students    TABLE     _   CREATE TABLE public.students (
    id integer NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public.students;
       public         heap r       postgres    false            �            1259    32864    students_courses    TABLE     �   CREATE TABLE public.students_courses (
    student_id integer NOT NULL,
    course_id integer NOT NULL,
    student_course_data date
);
 $   DROP TABLE public.students_courses;
       public         heap r       postgres    false            �            1259    32843    students_id_seq    SEQUENCE     �   CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.students_id_seq;
       public               postgres    false    220            �           0    0    students_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;
          public               postgres    false    219            1           2604    32856 
   courses id    DEFAULT     h   ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);
 9   ALTER TABLE public.courses ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    221    222    222            /           2604    32838    professors id    DEFAULT     n   ALTER TABLE ONLY public.professors ALTER COLUMN id SET DEFAULT nextval('public.professors_id_seq'::regclass);
 <   ALTER TABLE public.professors ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    217    218    218            0           2604    32847    students id    DEFAULT     j   ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);
 :   ALTER TABLE public.students ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    220    219    220            �          0    32853    courses 
   TABLE DATA           :   COPY public.courses (id, title, professor_id) FROM stdin;
    public               postgres    false    222   "       �          0    32835 
   professors 
   TABLE DATA           .   COPY public.professors (id, name) FROM stdin;
    public               postgres    false    218   �"       �          0    32844    students 
   TABLE DATA           ,   COPY public.students (id, name) FROM stdin;
    public               postgres    false    220   �"       �          0    32864    students_courses 
   TABLE DATA           V   COPY public.students_courses (student_id, course_id, student_course_data) FROM stdin;
    public               postgres    false    223   8#       �           0    0    courses_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.courses_id_seq', 9, true);
          public               postgres    false    221            �           0    0    professors_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.professors_id_seq', 6, true);
          public               postgres    false    217            �           0    0    students_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.students_id_seq', 12, true);
          public               postgres    false    219            7           2606    32858    courses courses_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.courses DROP CONSTRAINT courses_pkey;
       public                 postgres    false    222            3           2606    32842    professors professors_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.professors
    ADD CONSTRAINT professors_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.professors DROP CONSTRAINT professors_pkey;
       public                 postgres    false    218            9           2606    32868 &   students_courses students_courses_pkey 
   CONSTRAINT     w   ALTER TABLE ONLY public.students_courses
    ADD CONSTRAINT students_courses_pkey PRIMARY KEY (student_id, course_id);
 P   ALTER TABLE ONLY public.students_courses DROP CONSTRAINT students_courses_pkey;
       public                 postgres    false    223    223            5           2606    32851    students students_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.students DROP CONSTRAINT students_pkey;
       public                 postgres    false    220            :           2606    32859 !   courses courses_professor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_professor_id_fkey FOREIGN KEY (professor_id) REFERENCES public.professors(id);
 K   ALTER TABLE ONLY public.courses DROP CONSTRAINT courses_professor_id_fkey;
       public               postgres    false    218    4659    222            ;           2606    32874 0   students_courses students_courses_course_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.students_courses
    ADD CONSTRAINT students_courses_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(id);
 Z   ALTER TABLE ONLY public.students_courses DROP CONSTRAINT students_courses_course_id_fkey;
       public               postgres    false    222    223    4663            <           2606    32869 1   students_courses students_courses_student_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.students_courses
    ADD CONSTRAINT students_courses_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.students(id);
 [   ALTER TABLE ONLY public.students_courses DROP CONSTRAINT students_courses_student_id_fkey;
       public               postgres    false    223    220    4661            �      x�3�0�¾�/��~a�������
�_l 1.����7]�pa��rrq�$�$*'g��%��9/L�m��ya/��	�s���k�e�j�	�9�rY��k�e�j�W� =��      �   '   x�3�J,.��2��L�/�2�rM \S(����� ]W      �   D   x�3�H,K��2�N-JO��2�1L8]r3K�2+�L�j�`R�0�\�%T��L���2�+����� �7!�      �   F   x�]Ǳ�0�Z���ۻd�9Ң|���9��iS�^��K�X�����B�m8�<~w9���}��t&     