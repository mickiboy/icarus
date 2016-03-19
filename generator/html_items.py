#!/bin/env python3
#
# Icarus CMS
#
# (c) 2016 Daniel Jankowski


def get_header(title, stylesheet):
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">

    <title>{title}</title>

    <!-- Bootstrap core CSS -->
    <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="{stylesheet}" rel="stylesheet">


    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="./index.html">{title}</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="index.html">HOME</a></li>
            <li><a href="#about">ABOUT</a></li>
            <li><a href="#contact">CONTACT</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container">

      <div class="starter-template">
        <!-- content here ! -->
        <div class="row">
          <!-- blog posts row -->
          <div class="col-sm-9">
""".format(title=title.upper(), stylesheet=stylesheet)


def get_footer():
    return """
        </div>

      </div>

    </div><!-- /.container -->


    <!--<footer class="footer">
        <div class="copyright">
            © 2016 Daniel Jankowski
        </div>
    </footer>-->

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="../bootstrap/js/bootstrap.min.js"></script>
  </body>
</html>
"""


def get_sidebar(articles, archive):
    return """
        </div>
          <!-- blog information row -->
          <div class="col-sm-3">
            <div class="card card-sidebar">
              <h4 class="subheader">Latest articles</h4>
              <ul class="sidebar">
                {articles}
              </ul>
              <h4 class="subheader">Archive</h4>
              <ul class="sidebar">
                {archive}
              </ul>
            </div>
          </div>
""".format(articles=articles, archive=archive)


def get_blog_card(title, content, author, date, url):
    return """    
            <div class="card">
                <h2><a href="{url}" class="card-title">{title}</a></h2>
                <div class="blog-info">
                    <b>Date</b> {date} <b>Author</b> {author}
                </div>
                <div class="content">
                    {content}
                </div>
                <a href="{url}" class="read-more">READ MORE</a>
            </div>
""".format(url=url, title=title, content=content, date=date, author=author)


def get_article_card(title, content, author, date):
    return """    
            <div class="card-article">
                <h2>{title}</h2>
                <div class="blog-info">
                    <b>Date</b> {date} <b>Author</b> {author}
                </div>
                <div class="content-article">
                    {content}
                </div>
            </div>
""".format(title=title, content=content, date=date, author=author)
    return


def main():
    print(get_header("icarus", "./style.css"))
    print(get_footer())
    pass


if __name__ == '__main__':
    main()
