create table TBL_Users(

	UserID INT NOT NULL GENERATED ALWAYS AS IDENTITY,
	UserFullName varchar(40) NOT NULL,
	UserEmail varchar(40) NOT NULL,
	UserPassword varchar(150) NOT NULL,
	
	CONSTRAINT tbl_users_pkey PRIMARY KEY (UserID)

);



create table TBL_Posts(

	PostID INT NOT NULL GENERATED ALWAYS AS IDENTITY,
	UserID INT NOT null,
	PostTitle varchar(40) NOT NULL,
	PostCreateDate varchar(40) NOT NULL,
	PostContent varchar(40) NOT NULL

);

ALTER TABLE public.TBL_Posts ADD CONSTRAINT tbl_posts_user_id_fkey FOREIGN KEY (UserID) REFERENCES public.TBL_Users(UserID);
