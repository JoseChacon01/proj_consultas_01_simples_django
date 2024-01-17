insert into core_area (nome) values ('Informática');
insert into core_area (nome) values ('Eletromecânica');
insert into core_area (nome) values ('Eventos');

insert into core_publico (nome) values ('Discentes');
insert into core_publico (nome) values ('Docentes');
insert into core_publico (nome) values ('Técnicos');
insert into core_publico (nome) values ('Externo');

insert into core_curso (nome, data_inicio, vagas, area_id) values ('Android', '2023-01-10', 30, 1);
insert into core_curso (nome, data_inicio, vagas, area_id) values ('Web', '2024-03-01', 80, 1);
insert into core_curso (nome, data_inicio, vagas, area_id) values ('Solda', '2022-12-23', 40, 2);
insert into core_curso (nome, data_inicio, vagas, area_id) values ('Guia', '2023-04-19', 40, 3);

insert into core_curso_publicos (curso_id, publico_id) values(1, 1);
insert into core_curso_publicos (curso_id, publico_id) values(2, 1);
insert into core_curso_publicos (curso_id, publico_id) values(2, 2);
insert into core_curso_publicos (curso_id, publico_id) values(3, 4);
insert into core_curso_publicos (curso_id, publico_id) values(4, 1);
insert into core_curso_publicos (curso_id, publico_id) values(4, 2);
insert into core_curso_publicos (curso_id, publico_id) values(4, 3);
insert into core_curso_publicos (curso_id, publico_id) values(4, 4);