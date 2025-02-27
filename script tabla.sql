CREATE SCHEMA Gerontologia;
Use Gerontologia;

CREATE TABLE login(
id bigint primary key auto_increment,
contrasenaLogin varchar(100) not null,
rol varchar(50) default "N"
);

CREATE TABLE usuario(
id bigint primary key auto_increment,
nombres varchar(100) not null,
primer_apellido varchar(100) not null,
segundo_apellido varchar(100) not null,
documentoid varchar(50) not null,
celular varchar(30) default "N/A",
correo varchar(255) not null,
ciudad varchar(255) not null,
direccion varchar(255) not null
);

