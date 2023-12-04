CREATE DATABASE delivery_service;
-- delivery_service.`user` definition

CREATE TABLE delivery_service.user_entity (
	user_entity_id varchar(100) NOT NULL ,
	login varchar(100) NOT NULL,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	email varchar(100) NOT NULL,
	insert_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	update_date DATETIME NULL ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

ALTER TABLE delivery_service.user_entity ADD CONSTRAINT user_entity_PK PRIMARY KEY (user_entity_id);

CREATE TABLE delivery_service.delivery (
	delivery_id varchar(100) PRIMARY KEY NOT NULL,
	title varchar(100) NOT NULL,
	sender_id varchar(100) NOT NULL,
	applier_id varchar(100) NOT NULL,
	status varchar(100) NOT NULL,
    insert_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	update_date DATETIME NULL ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

ALTER TABLE delivery_service.delivery ADD CONSTRAINT delivery_PK PRIMARY KEY (delivery_id);
ALTER TABLE delivery_service.delivery ADD CONSTRAINT `user_entity_id_sender_id`
    FOREIGN KEY(sender_id) REFERENCES user_entity(user_entity_id);
ALTER TABLE delivery_service.delivery ADD CONSTRAINT `user_entity_id_applier_id`
    FOREIGN KEY(applier_id) REFERENCES user_entity(user_entity_id);

-- delivery_service.package definition

CREATE TABLE delivery_service.package (
	package_id varchar(100) PRIMARY KEY NOT NULL,
	title varchar(100) NOT NULL,
	description varchar(1000) NULL,
	delivery_id varchar(100) NOT NULL,
    insert_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	update_date DATETIME NULL ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

ALTER TABLE delivery_service.package ADD CONSTRAINT package_PK PRIMARY KEY (package_id);
ALTER TABLE delivery_service.package ADD CONSTRAINT `delivery_id_package_id`
    FOREIGN KEY(delivery_id) REFERENCES delivery(delivery_id);
