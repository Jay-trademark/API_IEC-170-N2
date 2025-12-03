create table if not exists geo(
    id integer auto_increment,
    lat varchar(10) not null,
    lng varchar(10) not null,

    constraint pk_geo primary key (id)
);

create table if not exists address(
    id integer auto_increment,
    street varchar(30) not null,
    suite varchar(10) not null,
    city varchar(20) not null,
    zipcode varchar(10) not null,
    geoid integer not null,

    constraint pk_address primary key (id),
    constraint fk_address_geo foreign key (geoid) references geo(id)
);

create table if not exists company(
    id integer auto_increment,
    name varchar(30) not null,
    catchphrase varchar(255) not null,
    bs varchar(100) not null,

    constraint pk_company primary key (id),
);

create table if not exists users(
    id integer auto_increment,
    name varchar(30) not null,
    username varchar(15) not null,
    email varchar(255) not null,
    phone varchar(25) not null,
    website varchar(255) not null,

    addressid integer not null,
    companyid integer not null,

    constraint pk_users primary key (id),
    constraint fk_users_address foreign key (addressid) references address(id),
    constraint fk_users_company foreign key (companyid) references company(id)
);

create table if not exists posts(
    id integer auto_increment,
    title varchar(50) not null,
    body varchar(255) not null,
    userid integer not null,

    constraint pk_posts primary key (id),
    constraint fk_posts_users foreign key (userid) references users(id)
);

