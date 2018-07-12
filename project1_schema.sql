-- Adminer 4.6.3-dev PostgreSQL dump

\connect "d4dhnjm6dcg7mm";

DROP TABLE IF EXISTS "comments";
DROP SEQUENCE IF EXISTS comments_id_seq;
CREATE SEQUENCE comments_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."comments" (
    "id" integer DEFAULT nextval('comments_id_seq') NOT NULL,
    "user_id" uuid,
    "location_id" uuid,
    "comment" character varying,
    CONSTRAINT "comments_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "comments_location_id_fkey" FOREIGN KEY (location_id) REFERENCES location(locationid) NOT DEFERRABLE,
    CONSTRAINT "comments_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"("UserID") NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "location";
CREATE TABLE "public"."location" (
    "locationid" uuid NOT NULL,
    "zipcode" character varying,
    "city" character varying,
    "state" character varying,
    "latitude" double precision,
    "longitude" double precision,
    "population" integer,
    CONSTRAINT "location_pkey" PRIMARY KEY ("locationid")
) WITH (oids = false);


DROP TABLE IF EXISTS "user";
CREATE TABLE "public"."user" (
    "UserID" uuid NOT NULL,
    "UserName" character varying(80) NOT NULL,
    "Password" character varying(64),
    CONSTRAINT "user_UserName_key" UNIQUE ("UserName"),
    CONSTRAINT "user_pkey" PRIMARY KEY ("UserID")
) WITH (oids = false);


-- 2018-07-12 14:39:37.38232+00
