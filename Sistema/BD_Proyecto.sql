create table datos_auto (
    idAuto varchar(100) primary key,
    placa varchar(10) not null,
    marca varchar(50),
    modelo varchar(30),
    color varchar(30),
    estatus_legar varchar(20),
    dueño varchar(255),
    verificacion BOOLEAN
);

create table bitacora (
    idBitacora INT PRIMARY key auto_increment,
    idQr VARCHAR(255),
    fechaHora DATETIME DEFAULT current_timestamp,
    motivo varchar(100),
    pdf varchar(200)
);