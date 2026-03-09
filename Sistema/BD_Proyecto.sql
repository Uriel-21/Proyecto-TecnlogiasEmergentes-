create table datos_auto (
    idAuto varchar(100) primary key,
    placa varchar(10) not null, 
    marca varchar (50),
    modelo varchar (30), 
    color varchar (30), 
    estatus_legar varchar(20), 
    verificacion BOOLEAN
);