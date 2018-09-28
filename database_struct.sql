drop table if exists sweetie.user;
create table sweetie.user(
	id int(11) auto_increment,
	open_id varchar(50) unique,
	couple_id int(11) default -1,
	egg_status int(3) default 0,
	egg_path varchar(100),
	task_proc int(3) default 0,
	primary key(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists sweetie.task;
create table sweetie.task(
	id int(11) auto_increment,
	u_id int(11) unique,
	answer varchar(50),
	standard varchar(50),
	img_path varchar(100),
	question_list varchar(50),
	primary key(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `question`;
CREATE TABLE `question`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `option_a` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `option_b` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `option_c` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `option_d` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

drop table if exists sweetie.conclusion;
create table sweetie.conclusion(
	id int(11) auto_increment,
	conclusion_type int(3),
	conclusion_text text,
	primary key(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


