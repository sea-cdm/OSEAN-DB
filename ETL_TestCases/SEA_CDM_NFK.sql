-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema seacdm
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `seacdm` DEFAULT CHARACTER SET utf8mb3 ;
SHOW WARNINGS;
USE `seacdm` ;

-- -----------------------------------------------------
-- Table `seacdm`.`analysis`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`analysis` (
  `analysis_id` INT NULL DEFAULT NULL,
  `documentation_id` INT NULL DEFAULT NULL,
  `group_id` TEXT NULL DEFAULT NULL,
  `analysis_name` TEXT NULL DEFAULT NULL,
  `analysis_name_id` TEXT NULL DEFAULT NULL,
  `input_data` TEXT NULL DEFAULT NULL,
  `input_data_idreference_id` TEXT NULL DEFAULT NULL,
  `reference_source` TEXT NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `assay_name` TEXT NULL DEFAULT NULL,
  `assay_type` TEXT NULL DEFAULT NULL,
  `assay_type_id` TEXT NULL DEFAULT NULL,
  `organism` TEXT NULL DEFAULT NULL,
  `imput_data` TEXT NULL DEFAULT NULL,
  `reference_id` INT NULL DEFAULT NULL,
  `reagents` TEXT NULL DEFAULT NULL,
  `platform` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`documentation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`documentation` (
  `documentation_id` INT NULL DEFAULT NULL,
  `study_id` INT NULL DEFAULT NULL,
  `document_name` TEXT NULL DEFAULT NULL,
  `document_type` TEXT NULL DEFAULT NULL,
  `document_type_id` TEXT NULL DEFAULT NULL,
  `documentation_source` TEXT NULL DEFAULT NULL,
  `source_id` INT NULL DEFAULT NULL,
  `reference_source` TEXT NULL DEFAULT NULL,
  `citation` TEXT NULL DEFAULT NULL,
  `citation_style` TEXT NULL DEFAULT NULL,
  `person_id` TEXT NULL DEFAULT NULL,
  `person_id_type` TEXT NULL DEFAULT NULL,
  `honorific` TEXT NULL DEFAULT NULL,
  `first_name` TEXT NULL DEFAULT NULL,
  `middle_name` TEXT NULL DEFAULT NULL,
  `last_name` TEXT NULL DEFAULT NULL,
  `person_role` TEXT NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`experiment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`experiment` (
  `experiment_id` INT NULL DEFAULT NULL,
  `study_id` INT NULL DEFAULT NULL,
  `experiment_type` TEXT NULL DEFAULT NULL,
  `experiment_type_id` TEXT NULL DEFAULT NULL,
  `experiment_control` INT NULL DEFAULT NULL,
  `source_id` TEXT NULL DEFAULT NULL,
  `reference_source` TEXT NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `experiment_name` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`group` (
  `group_id` INT NULL DEFAULT NULL,
  `experiment_id` INT NULL DEFAULT NULL,
  `group_type` TEXT NULL DEFAULT NULL,
  `group_size` TEXT NULL DEFAULT NULL,
  `reference_id` TEXT NULL DEFAULT NULL,
  `reference_source` TEXT NULL DEFAULT NULL,
  `max_age` DOUBLE NULL DEFAULT NULL,
  `min_age` DOUBLE NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`ignoretable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`ignoretable` (
  `idIgnoreTable` INT NOT NULL,
  PRIMARY KEY (`idIgnoreTable`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`intervention`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`intervention` (
  `intervention_id` INT NULL DEFAULT NULL,
  `experiment_id` INT NULL DEFAULT NULL,
  `organism_id` INT NULL DEFAULT NULL,
  `material` TEXT NULL DEFAULT NULL,
  `material_id` TEXT NULL DEFAULT NULL,
  `dosage` TEXT NULL DEFAULT NULL,
  `dosage_unit` TEXT NULL DEFAULT NULL,
  `dosage_unit_id` TEXT NULL DEFAULT NULL,
  `intervention_type` TEXT NULL DEFAULT NULL,
  `intervention_type_id` TEXT NULL DEFAULT NULL,
  `intervention_route` TEXT NULL DEFAULT NULL,
  `intervention_route_id` TEXT NULL DEFAULT NULL,
  `T0_defintion` TEXT NULL DEFAULT NULL,
  `intervention_time` INT NULL DEFAULT NULL,
  `intervention_unit` TEXT NULL DEFAULT NULL,
  `intervention_time_unit_id` TEXT NULL DEFAULT NULL,
  `source_id` TEXT NULL DEFAULT NULL,
  `reference_source` TEXT NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `T0_definition` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`material` (
  `material_id` INT NULL DEFAULT NULL,
  `material_name` TEXT NULL DEFAULT NULL,
  `material_name_id` TEXT NULL DEFAULT NULL,
  `organization` TEXT NULL DEFAULT NULL,
  `reference_id` TEXT NULL DEFAULT NULL,
  `reference_source` TEXT NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `reference` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`organism`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`organism` (
  `organism_id` INT NULL DEFAULT NULL,
  `group_id` TEXT NULL DEFAULT NULL,
  `experiment_id` INT NULL DEFAULT NULL,
  `species` TEXT NULL DEFAULT NULL,
  `species_id` TEXT NULL DEFAULT NULL,
  `type` TEXT NULL DEFAULT NULL,
  `type_id` TEXT NULL DEFAULT NULL,
  `age` TEXT NULL DEFAULT NULL,
  `age_unit` TEXT NULL DEFAULT NULL,
  `age_unit_id` TEXT NULL DEFAULT NULL,
  `sex` TEXT NULL DEFAULT NULL,
  `sex_id` TEXT NULL DEFAULT NULL,
  `reference_id` TEXT NULL DEFAULT NULL,
  `reference_source` TEXT NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`results`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`results` (
  `results_id` INT NULL DEFAULT NULL,
  `experiment_id` INT NULL DEFAULT NULL,
  `group_id` TEXT NULL DEFAULT NULL,
  `sample_id` INT NULL DEFAULT NULL,
  `analysis_name` TEXT NULL DEFAULT NULL,
  `analysis_id` INT NULL DEFAULT NULL,
  `original_assay_type` TEXT NULL DEFAULT NULL,
  `assay_id` TEXT NULL DEFAULT NULL,
  `analysis_type` TEXT NULL DEFAULT NULL,
  `datatype` TEXT NULL DEFAULT NULL,
  `datatype_id` TEXT NULL DEFAULT NULL,
  `file_access` TEXT NULL DEFAULT NULL,
  `file_type` TEXT NULL DEFAULT NULL,
  `replications` INT NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `document_id` TEXT NULL DEFAULT NULL,
  `original_assay_type_id` INT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`sample`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`sample` (
  `sample_id` INT NULL DEFAULT NULL,
  `group_id` TEXT NULL DEFAULT NULL,
  `organism_id` INT NULL DEFAULT NULL,
  `collection` TEXT NULL DEFAULT NULL,
  `collection_id` TEXT NULL DEFAULT NULL,
  `collection_time` DOUBLE NULL DEFAULT NULL,
  `collection_time_unit` TEXT NULL DEFAULT NULL,
  `collection_time_unit_id` TEXT NULL DEFAULT NULL,
  `T0_definition` TEXT NULL DEFAULT NULL,
  `expsample_type` TEXT NULL DEFAULT NULL,
  `expsample_type_id` TEXT NULL DEFAULT NULL,
  `expsample_reference_id` TEXT NULL DEFAULT NULL,
  `expsample_reference_name` TEXT NULL DEFAULT NULL,
  `biosample_type` TEXT NULL DEFAULT NULL,
  `biosample_type_id` TEXT NULL DEFAULT NULL,
  `biosample_reference_id` TEXT NULL DEFAULT NULL,
  `biosample_reference_name` TEXT NULL DEFAULT NULL,
  `replicates` TEXT NULL DEFAULT NULL,
  `expsample_source` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `seacdm`.`study`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`study` (
  `study_id` INT NULL DEFAULT NULL,
  `study_type` TEXT NULL DEFAULT NULL,
  `study_type_id` TEXT NULL DEFAULT NULL,
  `study_name` TEXT NULL DEFAULT NULL,
  `study_description` TEXT NULL DEFAULT NULL,
  `reference_id` TEXT NULL DEFAULT NULL,
  `reference_source` TEXT NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;



-- -----------------------------------------------------
-- Table `seacdm`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`users` (
  `idUsers` INT NOT NULL AUTO_INCREMENT,
  `User Name` VARCHAR(45) NULL DEFAULT NULL,
  `User Password` VARCHAR(45) NULL DEFAULT NULL,
  `UserPermissions` INT NULL DEFAULT NULL,
  `Userscol` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idUsers`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `seacdm`.`occurence`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `seacdm`.`users` (
  `occurence_id` INT NULL DEFAULT NULL,
  `organism_id` INT NULL DEFAULT NULL,
  `occurence_name_id` VARCHAR(45) NULL DEFAULT NULL,
  `occurence_severity` VARCHAR(45) NULL DEFAULT NULL,
  `occurence_start_time` VARCHAR(45) NULL DEFAULT NULL,
  `occurence_start_unit` VARCHAR(45) NULL DEFAULT NULL,
  `occurence_start_id` FLOAT NULL DEFAULT NULL,
  `occurence_end_unit` VARCHAR(45) NULL DEFAULT NULL,
  `occurence_end_unit_id` VARCHAR(45) NULL DEFAULT NULL,
  `source_id` VARCHAR(45) NULL DEFAULT NULL,
  `reference_source` VARCHAR(45) NULL DEFAULT NULL,
  `comments` VARCHAR(45) NULL DEFAULT NULL,)

ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;



SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
