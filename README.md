<h2 style="text-align: center;">Отчет по лабораторной работе №3</h2>
<h4>Введение</h4>
<p>В данной лабораторной работе будут рассмотрены 4 библиотеки для работы с базами данных (Psycopg2,SQLite, DuckDB, Pandas) на примере создания бенчмарка "4 queries".</p>
<p>Запуск осуществляется через один файл main.py, при этом используемые в запуске библиотеки могут изменяться в файле config.py.</p>
<h4>Запуск</h4>
<p>1) Установите python с официального сайта&nbsp;<a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>, а так же PostgreSQL при необходимости</p>
<p>2) Установите используемые библиотеки через терминал, используя следующую команду:&nbsp;<code>pip install duckdb gdown pandas psycopg2-binary</code></p>
<p dir="auto">3) Клонируйте репозиторий в нужную директорию, используя следующую команду:</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate"><code>https://github.com/Sonenka/dblab3.git</code></pre>
</div>
<p>4) Измените настройки под себя в файле config.py.</p>
<p>5) Запускайте программу.</p>
<p></p>
<h4>Результаты запуска</h4>
<p>Вывод программы:</p>
<p><img src="https://github.com/Sonenka/dblab3/blob/main/pictures/result.png" alt="вывод программы" /></p>
<p>Гистограмма и график, построенные на основе полученных данных (в папке files вы можете найти файл Excel со всеми графиками):</p>
<p><img src="https://github.com/Sonenka/dblab3/blob/main/pictures/graph.png" alt="Гистограмма" /></p>
<p><img src="https://github.com/Sonenka/dblab3/blob/main/pictures/graph.png" alt="Линейный график" /></p>
<p></p>
<h4>Отчет</h4>
<p>По полученным данным можно сделать выводы о каждой из библиотек:</p>
<p>1)&nbsp;Psycopg2</p>
<p>По моему мнению, это самая неудобная в использовании библеотека из представленных, так как помимо написания самого кода, необходимо было подключаться к PostgreSQL.</p>
<p>2)&nbsp;SQLite</p>
<p>3)&nbsp;DuckDB</p>
<p>4)&nbsp;Pandas</p>
