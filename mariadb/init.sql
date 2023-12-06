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
	delivery_id varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	sender_id varchar(100) NOT NULL,
	applier_id varchar(100) NOT NULL,
	status varchar(100) NOT NULL,
    insert_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	update_date DATETIME NULL ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

ALTER TABLE delivery_service.delivery ADD CONSTRAINT delivery_PK PRIMARY KEY (delivery_id);
ALTER TABLE delivery_service.delivery ADD CONSTRAINT user_entity_id_sender_id
    FOREIGN KEY(sender_id) REFERENCES user_entity(user_entity_id);
ALTER TABLE delivery_service.delivery ADD CONSTRAINT user_entity_id_applier_id
    FOREIGN KEY(applier_id) REFERENCES user_entity(user_entity_id);

-- delivery_service.package definition

CREATE TABLE delivery_service.package (
	package_id varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	description varchar(1000) NULL,
	delivery_id varchar(100) NOT NULL,
    insert_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	update_date DATETIME NULL ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

ALTER TABLE delivery_service.package ADD CONSTRAINT package_PK PRIMARY KEY (package_id);
ALTER TABLE delivery_service.package ADD CONSTRAINT delivery_id_package_id
    FOREIGN KEY(delivery_id) REFERENCES delivery(delivery_id);






-- inserts user_entity
INSERT INTO delivery_service.user_entity
(user_entity_id, login, first_name, last_name, email, insert_date, update_date)
VALUES('8722f110-9467-11ee-8e92-0242ac120001', 'ivan1', 'Ivan', 'Ivanov',  'ivan@mail.ru', current_timestamp(), '0000-00-00 00:00:00');
INSERT INTO delivery_service.user_entity
(user_entity_id, login, first_name, last_name, email, insert_date, update_date)
VALUES('8722f110-9467-11ee-8e92-0242ac120002', 'petr1', 'Petr', 'Petrov',  'petr@mail.ru', current_timestamp(), '0000-00-00 00:00:00');
INSERT INTO delivery_service.user_entity
(user_entity_id, login, first_name, last_name, email, insert_date, update_date)
VALUES('8722f110-9467-11ee-8e92-0242ac120003', 'ilya1', 'Ilya', 'Vasilev', 'ilya@mail.ru', current_timestamp(), '0000-00-00 00:00:00');


-- inserts delivery
INSERT INTO delivery_service.delivery
(delivery_id, title, sender_id, applier_id, status, insert_date, update_date)
VALUES('fa1f2110-9467-11ee-8e92-0242ac120001', 'delivery one',   '8722f110-9467-11ee-8e92-0242ac120001', '8722f110-9467-11ee-8e92-0242ac120002', 'READY', current_timestamp(), '0000-00-00 00:00:00');
INSERT INTO delivery_service.delivery
(delivery_id, title, sender_id, applier_id, status, insert_date, update_date)
VALUES('fa1f2110-9467-11ee-8e92-0242ac120002', 'delivery two',   '8722f110-9467-11ee-8e92-0242ac120002', '8722f110-9467-11ee-8e92-0242ac120003', 'PACKAGING', current_timestamp(), '0000-00-00 00:00:00');
INSERT INTO delivery_service.delivery
(delivery_id, title, sender_id, applier_id, status, insert_date, update_date)
VALUES('fa1f2110-9467-11ee-8e92-0242ac120003', 'delivery three', '8722f110-9467-11ee-8e92-0242ac120003', '8722f110-9467-11ee-8e92-0242ac120001', 'GOT', current_timestamp(), '0000-00-00 00:00:00');


-- inserts package
INSERT INTO delivery_service.package
(package_id, title, description, delivery_id, insert_date, update_date)
VALUES('vf7f2110-9467-11ee-8e92-0242ac120001', 'PC', '11400f',   'fa1f2110-9467-11ee-8e92-0242ac120001', current_timestamp(), '0000-00-00 00:00:00');
INSERT INTO delivery_service.package
(package_id, title, description, delivery_id, insert_date, update_date)
VALUES('vf7f2110-9467-11ee-8e92-0242ac120002', 'T-shirt', null,  'fa1f2110-9467-11ee-8e92-0242ac120001', current_timestamp(), '0000-00-00 00:00:00');
INSERT INTO delivery_service.package
(package_id, title, description, delivery_id, insert_date, update_date)
VALUES('vf7f2110-9467-11ee-8e92-0242ac120003', 'Monitor', null,  'fa1f2110-9467-11ee-8e92-0242ac120001', current_timestamp(), '0000-00-00 00:00:00');
INSERT INTO delivery_service.package
(package_id, title, description, delivery_id, insert_date, update_date)
VALUES('vf7f2110-9467-11ee-8e92-0242ac120004', 'Phone', 'Meizu', 'fa1f2110-9467-11ee-8e92-0242ac120002', current_timestamp(), '0000-00-00 00:00:00');
INSERT INTO delivery_service.package
(package_id, title, description, delivery_id, insert_date, update_date)
VALUES('vf7f2110-9467-11ee-8e92-0242ac120005', 'Suit', NULL,     'fa1f2110-9467-11ee-8e92-0242ac120003', current_timestamp(), '0000-00-00 00:00:00');


