from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
CREATE TABLE IF NOT EXISTS cars (
	id int4 NOT NULL DEFAULT nextval('car_id_seq'::regclass),
	title varchar NOT NULL,
	"content" varchar NOT NULL,
	ad_id uuid NULL,
	advert_id uuid NULL,
	url varchar NULL,
	price float8 NULL,
	make varchar NULL,
	model varchar NULL,
	color varchar NULL,
	"year" int4 NULL,
	city varchar NULL,
	post_code varchar NULL,
	mileage int4 NULL,
	doors int4 NULL,
	fuel varchar NULL,
	transmission varchar NULL,
	body_style varchar NULL,
	engine_size int4 NULL,
	seats int4 NULL,
	hero_image varchar NULL,
	"date" timestamp NULL,
	car_type varchar NULL,
	dealer_domain varchar NULL,
	dealer_name varchar NULL,
	priority int4 NULL,
	seller_type varchar NULL,
	vrm varchar NULL,
	active bool NULL,
	created timestamp NULL,
	CONSTRAINT cars_pkey PRIMARY KEY (id)
);
CREATE INDEX IF NOT EXISTS cars_id_idx ON cars USING btree (id);
CREATE TABLE IF NOT EXISTS car_pictures (
	id int4 NOT NULL DEFAULT nextval('car_picture_id_seq'::regclass),
	car_id int4 NOT NULL,
	url varchar NOT NULL,
	active bool NOT NULL,
	CONSTRAINT car_pictures_pkey PRIMARY KEY (id)
);
CREATE INDEX IF NOT EXISTS car_pictures_id_idx ON car_pictures USING btree (id);
ALTER TABLE car_pictures ADD CONSTRAINT car_pictures_car_id_fkey FOREIGN KEY (car_id) REFERENCES cars(id);
"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
