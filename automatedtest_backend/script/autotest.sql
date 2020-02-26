-- MySQL dump 10.13  Distrib 5.7.13, for Win64 (x86_64)
--
-- Host: localhost    Database: autotest
-- ------------------------------------------------------
-- Server version	5.7.13-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `api_user`
--

DROP TABLE IF EXISTS `api_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `number` varchar(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_user`
--

LOCK TABLES `api_user` WRITE;
/*!40000 ALTER TABLE `api_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add API用户',6,'add_apiuser'),(22,'Can change API用户',6,'change_apiuser'),(23,'Can delete API用户',6,'delete_apiuser'),(24,'Can view API用户',6,'view_apiuser'),(25,'Can add 用户',7,'add_user'),(26,'Can change 用户',7,'change_user'),(27,'Can delete 用户',7,'delete_user'),(28,'Can view 用户',7,'view_user'),(29,'Can add 数据库',8,'add_projectdataserver'),(30,'Can change 数据库',8,'change_projectdataserver'),(31,'Can delete 数据库',8,'delete_projectdataserver'),(32,'Can view 数据库',8,'view_projectdataserver'),(33,'Can add 项目环境',9,'add_projectenvironment'),(34,'Can change 项目环境',9,'change_projectenvironment'),(35,'Can delete 项目环境',9,'delete_projectenvironment'),(36,'Can view 项目环境',9,'view_projectenvironment'),(37,'Can add 项目管理',10,'add_projectmanager'),(38,'Can change 项目管理',10,'change_projectmanager'),(39,'Can delete 项目管理',10,'delete_projectmanager'),(40,'Can view 项目管理',10,'view_projectmanager'),(41,'Can add 服务器',11,'add_projectserver'),(42,'Can change 服务器',11,'change_projectserver'),(43,'Can delete 服务器',11,'delete_projectserver'),(44,'Can view 服务器',11,'view_projectserver'),(45,'Can add 接口',12,'add_interfacemodel'),(46,'Can change 接口',12,'change_interfacemodel'),(47,'Can delete 接口',12,'delete_interfacemodel'),(48,'Can view 接口',12,'view_interfacemodel'),(49,'Can add 模块',13,'add_interfacemodule'),(50,'Can change 模块',13,'change_interfacemodule'),(51,'Can delete 模块',13,'delete_interfacemodule'),(52,'Can view 模块',13,'view_interfacemodule'),(53,'Can add 关键字',14,'add_keysmodel'),(54,'Can change 关键字',14,'change_keysmodel'),(55,'Can delete 关键字',14,'delete_keysmodel'),(56,'Can view 关键字',14,'view_keysmodel'),(57,'Can add 数据源',15,'add_casefile'),(58,'Can change 数据源',15,'change_casefile'),(59,'Can delete 数据源',15,'delete_casefile'),(60,'Can view 数据源',15,'view_casefile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datasources_db`
--

DROP TABLE IF EXISTS `datasources_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datasources_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `title` varchar(30) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `exclelist` longtext,
  `interface_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `interface_id` (`interface_id`),
  KEY `datasources_db_project_id_620b0765_fk_project_manager_id` (`project_id`),
  CONSTRAINT `datasources_db_interface_id_63aeebe5_fk_interface_db_id` FOREIGN KEY (`interface_id`) REFERENCES `interface_db` (`id`),
  CONSTRAINT `datasources_db_project_id_620b0765_fk_project_manager_id` FOREIGN KEY (`project_id`) REFERENCES `project_manager` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datasources_db`
--

LOCK TABLES `datasources_db` WRITE;
/*!40000 ALTER TABLE `datasources_db` DISABLE KEYS */;
INSERT INTO `datasources_db` VALUES (1,'2020-01-13 07:42:44.800823','2020-01-13 07:43:05.943246','数据源1','case/根据五要素新增客户_GmUsNQo.xlsx','[{\"other\":{\"TestName\":{\"desc\":\"aaaa\",\"postion\":\"other\",\"value\":\"\\u65b0\\u589e\\u5ba2\\u6237_\\u4e0d\\u5b58\\u5728\\u7684\\u4e94\\u8981\\u7d20\"},\"TestDesc\":{\"desc\":\"\\u7528\\u4f8b\\u8bf4\\u660e\",\"postion\":\"other\",\"value\":\"TC001_\\u8f93\\u5165\\u4e0d\\u5b58\\u5728\\u7684\\u4e94\\u8981\\u7d20\"},\"TestTags\":{\"desc\":\"\\u7528\\u4f8b\\u6807\\u7b7e\",\"postion\":\"other\",\"value\":\"Sprint2,CustomerCenter,Positive,AddCustomer\"}},\"id\":4,\"var\":{\"$.fullName\":{\"desc\":\"fullName\",\"postion\":\"body\",\"value\":\"\\u6f06\\u770b\\u7684\"},\"$.genderCode\":{\"desc\":\"genderCode\",\"postion\":\"body\",\"value\":\"M\"},\"$.birthDate\":{\"desc\":\"birthDate\",\"postion\":\"body\",\"value\":\"2000-01-12\"},\"$.governmentIssuedId.typeCode\":{\"desc\":\"typeCode\",\"postion\":\"body\",\"value\":\"01\"},\"$.governmentIssuedId.number\":{\"desc\":\"number\",\"postion\":\"body\",\"value\":\"110101200001120017\"},\"status_code\":{\"desc\":\"\\u65ad\\u8a00status_code\",\"postion\":\"assert\",\"value\":200.0},\"fullName\":{\"desc\":\"fullName\",\"postion\":\"prepare\",\"value\":\"\\u6f06\\u770b\\u7684\"},\"genderCode\":{\"desc\":\"genderCode\",\"postion\":\"prepare\",\"value\":\"M\"},\"birthDate\":{\"desc\":\"birthDate\",\"postion\":\"prepare\",\"value\":\"2000-01-12\"},\"typeCode\":{\"desc\":\"typeCode\",\"postion\":\"prepare\",\"value\":\"01\"},\"number\":{\"desc\":\"number\",\"postion\":\"prepare\",\"value\":\"110101200001120017\"}}},{\"other\":{\"TestName\":{\"desc\":\"aaaa\",\"postion\":\"other\",\"value\":\"\\u65b0\\u589e\\u5ba2\\u6237_\\u51fa\\u751f\\u65e5\\u671f\\u683c\\u5f0f\\u4e3ayyyy-MM-dd\"},\"TestDesc\":{\"desc\":\"\\u7528\\u4f8b\\u8bf4\\u660e\",\"postion\":\"other\",\"value\":\"TC063_\\u51fa\\u751f\\u65e5\\u671f\\u683c\\u5f0f\\u4e3ayyyy-MM-dd\"},\"TestTags\":{\"desc\":\"\\u7528\\u4f8b\\u6807\\u7b7e\",\"postion\":\"other\",\"value\":\"Sprint2,CustomerCenter,Positive,AddCustomer\"}},\"id\":5,\"var\":{\"$.fullName\":{\"desc\":\"fullName\",\"postion\":\"body\",\"value\":\"\\u9e3f\\u7406\\u7ed9\"},\"$.genderCode\":{\"desc\":\"genderCode\",\"postion\":\"body\",\"value\":\"M\"},\"$.birthDate\":{\"desc\":\"birthDate\",\"postion\":\"body\",\"value\":\"2000-01-12\"},\"$.governmentIssuedId.typeCode\":{\"desc\":\"typeCode\",\"postion\":\"body\",\"value\":\"01\"},\"$.governmentIssuedId.number\":{\"desc\":\"number\",\"postion\":\"body\",\"value\":\"110101200001120017\"},\"status_code\":{\"desc\":\"\\u65ad\\u8a00status_code\",\"postion\":\"assert\",\"value\":200.0},\"fullName\":{\"desc\":\"fullName\",\"postion\":\"prepare\",\"value\":\"\\u9e3f\\u7406\\u7ed9\"},\"genderCode\":{\"desc\":\"genderCode\",\"postion\":\"prepare\",\"value\":\"M\"},\"birthDate\":{\"desc\":\"birthDate\",\"postion\":\"prepare\",\"value\":\"2000-01-12\"},\"typeCode\":{\"desc\":\"typeCode\",\"postion\":\"prepare\",\"value\":\"01\"},\"number\":{\"desc\":\"number\",\"postion\":\"prepare\",\"value\":\"110101200001120017\"}}}]',1,1);
/*!40000 ALTER TABLE `datasources_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_tb_users_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_tb_users_id` FOREIGN KEY (`user_id`) REFERENCES `tb_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-01-13 07:30:42.433256','2','zhangwei',1,'[{\"added\": {}}]',7,1),(2,'2020-01-13 07:30:50.785730','2','zhangwei',2,'[]',7,1),(3,'2020-01-13 07:40:09.081489','1','变量',1,'[{\"added\": {}}]',14,1),(4,'2020-01-13 07:40:36.772257','2','JSON参数',1,'[{\"added\": {}}]',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(15,'datasourcemanagement','casefile'),(12,'interfacemanagement','interfacemodel'),(13,'interfacemanagement','interfacemodule'),(14,'interfacemanagement','keysmodel'),(8,'projectmanagent','projectdataserver'),(9,'projectmanagent','projectenvironment'),(10,'projectmanagent','projectmanager'),(11,'projectmanagent','projectserver'),(5,'sessions','session'),(6,'user','apiuser'),(7,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-01-13 07:20:57.473666'),(2,'contenttypes','0002_remove_content_type_name','2020-01-13 07:20:57.569588'),(3,'auth','0001_initial','2020-01-13 07:20:57.661027'),(4,'auth','0002_alter_permission_name_max_length','2020-01-13 07:20:57.912775'),(5,'auth','0003_alter_user_email_max_length','2020-01-13 07:20:57.920727'),(6,'auth','0004_alter_user_username_opts','2020-01-13 07:20:57.926710'),(7,'auth','0005_alter_user_last_login_null','2020-01-13 07:20:57.933690'),(8,'auth','0006_require_contenttypes_0002','2020-01-13 07:20:57.937680'),(9,'auth','0007_alter_validators_add_error_messages','2020-01-13 07:20:57.943694'),(10,'auth','0008_alter_user_username_max_length','2020-01-13 07:20:57.950659'),(11,'auth','0009_alter_user_last_name_max_length','2020-01-13 07:20:57.957665'),(12,'auth','0010_alter_group_name_max_length','2020-01-13 07:20:58.009555'),(13,'auth','0011_update_proxy_permissions','2020-01-13 07:20:58.015539'),(14,'user','0001_initial','2020-01-13 07:20:58.137727'),(15,'admin','0001_initial','2020-01-13 07:20:58.441188'),(16,'projectmanagent','0001_initial','2020-01-13 07:20:58.736150'),(17,'interfacemanagement','0001_initial','2020-01-13 07:20:58.890988'),(18,'datasourcemanagement','0001_initial','2020-01-13 07:20:58.933909'),(19,'datasourcemanagement','0002_casefile_interface','2020-01-13 07:20:58.979788'),(20,'datasourcemanagement','0003_casefile_project','2020-01-13 07:20:59.089583'),(21,'interfacemanagement','0002_auto_20200113_1520','2020-01-13 07:20:59.310519'),(22,'projectmanagent','0002_auto_20200113_1520','2020-01-13 07:20:59.676825'),(23,'sessions','0001_initial','2020-01-13 07:20:59.842403'),(24,'projectmanagent','0003_auto_20200113_1528','2020-01-13 07:29:06.935152');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4cas4hoxbcyg3zudl7l794luyrw8735a','MjQzYzQ0MDMyNTAzOGVlMDIzM2JjMmE5OGIxM2ZkMzM0ZDUxZDkzZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyYjI5MGFlMTVmMDQxYTRlYTc2ZjBkOWIxZWU3ZDJlYjNkMzc0OTA3In0=','2020-01-27 07:26:00.590858');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interface_db`
--

DROP TABLE IF EXISTS `interface_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interface_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `modifier` varchar(20) NOT NULL,
  `desc` longtext,
  `path_url` varchar(200) DEFAULT NULL,
  `port` int(11) DEFAULT NULL,
  `request_protocol` int(11) DEFAULT NULL,
  `request_way` int(11) DEFAULT NULL,
  `bodyformat` int(11) DEFAULT NULL,
  `bodymessageformat` int(11) DEFAULT NULL,
  `params` longtext,
  `headerparams` longtext,
  `bodyparams` longtext,
  `preprocessing` longtext,
  `postprocessing` longtext,
  `assertion` longtext,
  `intermodule_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_db_intermodule_id_f6c10138_fk_module_db_id` (`intermodule_id`),
  KEY `interface_db_project_id_06f56504_fk_project_manager_id` (`project_id`),
  CONSTRAINT `interface_db_intermodule_id_f6c10138_fk_module_db_id` FOREIGN KEY (`intermodule_id`) REFERENCES `module_db` (`id`),
  CONSTRAINT `interface_db_project_id_06f56504_fk_project_manager_id` FOREIGN KEY (`project_id`) REFERENCES `project_manager` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interface_db`
--

LOCK TABLES `interface_db` WRITE;
/*!40000 ALTER TABLE `interface_db` DISABLE KEYS */;
INSERT INTO `interface_db` VALUES (1,'接口1','2020-01-13 07:42:02.151422','2020-01-13 07:42:02.151422','暂定','描述1','/url',1234,2,3,3,3,'[{\"paramname\":\"a\",\"variable_name\":\"aa\",\"desc\":\"dec\"}]','[{\"paramname\":\"b\",\"variable_name\":\"bb\",\"desc\":\"desc\"}]','{\"name\":\"zz\"}',NULL,NULL,NULL,1,1);
/*!40000 ALTER TABLE `interface_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `keys_db`
--

DROP TABLE IF EXISTS `keys_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `keys_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `value` varchar(100) DEFAULT NULL,
  `count` int(11) NOT NULL,
  `params_constraint` longtext NOT NULL,
  `keytype` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keys_db`
--

LOCK TABLES `keys_db` WRITE;
/*!40000 ALTER TABLE `keys_db` DISABLE KEYS */;
INSERT INTO `keys_db` VALUES (1,'变量','$VAR',1,'[{\"paramname\":\"name\"},{\"paramname\":\"height\"}]',1),(2,'JSON参数','JSON_GET',1,'[{\"paramname\":\"name\"},{\"paramname\":\"height\"}]',1);
/*!40000 ALTER TABLE `keys_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `module_db`
--

DROP TABLE IF EXISTS `module_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `module_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `top` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `module_db_project_id_c0788f8a_fk_project_manager_id` (`project_id`),
  CONSTRAINT `module_db_project_id_c0788f8a_fk_project_manager_id` FOREIGN KEY (`project_id`) REFERENCES `project_manager` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module_db`
--

LOCK TABLES `module_db` WRITE;
/*!40000 ALTER TABLE `module_db` DISABLE KEYS */;
INSERT INTO `module_db` VALUES (1,'模块1',0,0,1);
/*!40000 ALTER TABLE `module_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_db`
--

DROP TABLE IF EXISTS `project_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `custom_variable` varchar(30) NOT NULL,
  `ip` char(39) DEFAULT NULL,
  `port` int(11) NOT NULL,
  `pwd` varchar(20) NOT NULL,
  `username` varchar(30) NOT NULL,
  `pro_env_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_db_pro_env_id_5cb891df_fk_project_env_id` (`pro_env_id`),
  CONSTRAINT `project_db_pro_env_id_5cb891df_fk_project_env_id` FOREIGN KEY (`pro_env_id`) REFERENCES `project_env` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_db`
--

LOCK TABLES `project_db` WRITE;
/*!40000 ALTER TABLE `project_db` DISABLE KEYS */;
INSERT INTO `project_db` VALUES (1,'服务器3','varr','192.168.1.1',1234,'123','zw',1),(2,'服务器4','vvvv','192.168.1.2',1234,'321','zw2',1);
/*!40000 ALTER TABLE `project_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_env`
--

DROP TABLE IF EXISTS `project_env`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_env` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `env` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_env_project_id_env_9c209f23_uniq` (`project_id`,`env`),
  CONSTRAINT `project_env_project_id_4d132c86_fk_project_manager_id` FOREIGN KEY (`project_id`) REFERENCES `project_manager` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_env`
--

LOCK TABLES `project_env` WRITE;
/*!40000 ALTER TABLE `project_env` DISABLE KEYS */;
INSERT INTO `project_env` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,1,2),(6,2,2),(7,3,2),(8,4,2),(9,1,3),(10,2,3),(11,3,3),(12,4,3),(13,1,4),(14,2,4),(15,3,4),(16,4,4);
/*!40000 ALTER TABLE `project_env` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_manager`
--

DROP TABLE IF EXISTS `project_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `start_time` varchar(50) NOT NULL,
  `end_time` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `level` int(11) NOT NULL,
  `desc` longtext,
  `is_delete` tinyint(1) NOT NULL,
  `person_charge_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_manager_person_charge_id_46c3fd1d_fk_tb_users_id` (`person_charge_id`),
  CONSTRAINT `project_manager_person_charge_id_46c3fd1d_fk_tb_users_id` FOREIGN KEY (`person_charge_id`) REFERENCES `tb_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_manager`
--

LOCK TABLES `project_manager` WRITE;
/*!40000 ALTER TABLE `project_manager` DISABLE KEYS */;
INSERT INTO `project_manager` VALUES (1,'项目1','1577894400000','1578326400000',1,3,'desc',0,NULL),(2,'项目2','1578412800000','1579708800000',1,2,'desc2',0,NULL),(3,'项目3','1578499200000','1579795200000',1,1,'desc3',0,NULL),(4,'项目4','1578585600000','1579881600000',1,2,'desc4',0,NULL);
/*!40000 ALTER TABLE `project_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_server`
--

DROP TABLE IF EXISTS `project_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `ip_url` varchar(50) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `custom_variable` varchar(30) NOT NULL,
  `pro_env_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_server_pro_env_id_19a23bfb_fk_project_env_id` (`pro_env_id`),
  CONSTRAINT `project_server_pro_env_id_19a23bfb_fk_project_env_id` FOREIGN KEY (`pro_env_id`) REFERENCES `project_env` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_server`
--

LOCK TABLES `project_server` WRITE;
/*!40000 ALTER TABLE `project_server` DISABLE KEYS */;
INSERT INTO `project_server` VALUES (1,'服务名1','url','1','2',1),(2,'服务名2','url','3','4',1);
/*!40000 ALTER TABLE `project_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_users`
--

DROP TABLE IF EXISTS `tb_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_users`
--

LOCK TABLES `tb_users` WRITE;
/*!40000 ALTER TABLE `tb_users` DISABLE KEYS */;
INSERT INTO `tb_users` VALUES (1,'pbkdf2_sha256$150000$rPaH8bgyxQ9l$s84U/01sSp9MVyIw1d6S+3TXsJS/1bjFlhbtFo0MRbE=','2020-01-13 07:26:00.573920',1,'zhousheng','','','zhouosheng@163.com',1,1,'2020-01-13 07:22:24.770388',''),(2,'zhangwei',NULL,0,'zhangwei','wei','zhang','zhang@163.com',0,1,'2020-01-13 07:29:00.000000','18701026595');
/*!40000 ALTER TABLE `tb_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_users_groups`
--

DROP TABLE IF EXISTS `tb_users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_users_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tb_users_groups_user_id_group_id_5a177a84_uniq` (`user_id`,`group_id`),
  KEY `tb_users_groups_group_id_04d64563_fk_auth_group_id` (`group_id`),
  CONSTRAINT `tb_users_groups_group_id_04d64563_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `tb_users_groups_user_id_5f9e3ed0_fk_tb_users_id` FOREIGN KEY (`user_id`) REFERENCES `tb_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_users_groups`
--

LOCK TABLES `tb_users_groups` WRITE;
/*!40000 ALTER TABLE `tb_users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_users_user_permissions`
--

DROP TABLE IF EXISTS `tb_users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_users_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tb_users_user_permissions_user_id_permission_id_064c2ef6_uniq` (`user_id`,`permission_id`),
  KEY `tb_users_user_permis_permission_id_b9b3ac94_fk_auth_perm` (`permission_id`),
  CONSTRAINT `tb_users_user_permis_permission_id_b9b3ac94_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `tb_users_user_permissions_user_id_2726c819_fk_tb_users_id` FOREIGN KEY (`user_id`) REFERENCES `tb_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_users_user_permissions`
--

LOCK TABLES `tb_users_user_permissions` WRITE;
/*!40000 ALTER TABLE `tb_users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-13 17:30:59
