from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """CREATE TABLE ads (
	id serial4 NOT NULL,
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
	CONSTRAINT car_pkey PRIMARY KEY (id)
);
CREATE TABLE ad_pictures (
	id serial4 NOT NULL,
	ad_id int4 NOT NULL,
	url varchar NOT NULL,
	active bool NOT NULL,
	CONSTRAINT ad_picture_pkey PRIMARY KEY (id),
	CONSTRAINT ad_picture_ad_id_fkey FOREIGN KEY (ad_id) REFERENCES ads(id)
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
    DROP TABLE ad_pictures;
    DROP TABLE ads;
        """
