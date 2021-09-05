drop database TFB103d_azure;
create database TFB103d_azure;

use TFB103d_azure;


create table movie(
	movie_id varchar(36) NOT NULL PRIMARY KEY,
   movie_name varchar(50),
   movie_desc varchar(10000),
   imdb_rating float(2,1),
   tomato_rating float(2,1),
   kimo_rating float(2,1)
);

create table movie_actor_ref(
	am_id varchar(36) NOT NULL PRIMARY KEY,
   actor_name varchar(50),
   movie_id varchar(36),
   movie_name varchar(50),
   FOREIGN KEY (movie_id) REFERENCES movie(movie_id) 
);

insert into movie values(
'b24151bd-6689-487f-a328-8a0b434175d1',
'Inception',
'超強檔新片《全面啟動》是《黑暗騎士》大導演克里斯多夫諾蘭執導的原創科幻動作片，找來陣容堅強的國際卡司，描述跨越全球的旅程，以及進入私密且無窮無盡的夢境世界。唐姆柯比（李奧納多狄卡皮歐 飾）是一名技術高超的神偷，不過他偷竊的目標物絕對涉及最危險、最神秘的範疇，他專門趁目標對象呈睡眠狀態之際，也就是人類心智最脆弱時，深入其潛意識偷取寶貴的秘密。柯比的罕見能力使他成為邪惡新世界中企業間諜活動夢寐以求的專家，然而這也使他成為國際逃犯，導致他失去所愛的一切。如今，柯比獲得重新開始的機會，最後這一份工作能使他找回他原本的人生，不過唯有他具備完成這項不可能任務的才能，代號：「開端」（inception）。柯比這次將不再執行他嫻熟的... 詳全文',
'8.8',
'8.0',
'4.7'
);

insert into movie values(
'178daa07-d43f-489e-b09a-5f65e42f4f27',
'Venom',
'最新電影《猛毒》由《屍樂園》的魯賓弗來舍執導，並找來《黑暗騎士：黎明昇起》英倫男星湯姆哈迪、《大娛樂家》蜜雪兒威廉斯與《星際大戰外傳：俠盜一號》里茲阿邁德等重量級卡司組成黃金陣容，自《蜘蛛人3》出現就備受關注的最強宿敵「猛毒」身為外星有機生命體，需尋找宿主結合才能生存，能賦予宿主超越想像的強大能量，亦正亦邪的角色特質更讓「猛毒」成為漫威漫畫裡最受歡迎的角色之一。',
'6.7',
'6.1',
'4.1'
);

insert into movie values(
'a3dd37a4-622e-4000-a26f-2973b289fef5',
'The Revenant',
'★《鳥人》金獎導演最新作品 強勢問鼎2016年奧斯卡所有獎項
★《華爾街之狼》李奧納多狄卡皮歐 2016奧斯卡影帝首選佳作
★《瘋狂麥斯》湯姆哈迪 完美詮釋黑暗人性
★磅礡冒險史詩 驚險求生浩瀚場面直逼《地心引力》《星際效應》
★遠赴阿根廷加拿大荒野 實境自然光拍攝 啟動超越特效的視覺震撼
★美國家喻戶曉傳奇獵人 真實野地求生故事改編

美國，19世紀初，拓荒年代，在文明邊境遊蕩著一群靠動物皮毛賺錢的獵人。其中一名獵人「休格拉斯」跟隨團隊翻山越嶺，在途中意外遭受野生灰熊的攻擊而受重傷，同行夥伴們卻為了保性命拋下他自生自滅。僥倖存活下來的他決定將千里跋涉討回公道，並踏上一趟前所未見，奇蹟般的旅程。',
'8.0',
'7.9',
'4.2'
);

insert into movie_actor_ref values(
	'4b68ac09-2875-4033-a5da-baa745009739',
    'Tom Hardy',
    'b24151bd-6689-487f-a328-8a0b434175d1',
    'Inception'
);

insert into movie_actor_ref values(
	'f8c3f507-7b5c-42f5-815b-8b92051c9fcb',
    'Tom Hardy',
    '178daa07-d43f-489e-b09a-5f65e42f4f27',
    'Venom'
);

insert into movie_actor_ref values(
	'4f9d8667-ef23-4893-a24f-70412d59f5ae',
    'Leonardo DiCaprio',
    'b24151bd-6689-487f-a328-8a0b434175d1',
    'Inception'
);

insert into movie_actor_ref values(
	'668ca26c-378a-4b0a-9a31-5de0e6833090',
    'Leonardo DiCaprio',
    'a3dd37a4-622e-4000-a26f-2973b289fef5',
    'The Revenant'
);

select movie_name from movie_actor_ref where actor_name in ('Tom Hardy','Leonardo DiCaprio')  group by movie_name having count(actor_name)=2;


