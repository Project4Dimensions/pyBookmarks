<!DOCTYPE html>
<html lang="en" class="h-100">
% include(tpl + 'head', title=title + 'search')
<body class="d-flex flex-column h-100">
<main role="main" class="container mt-3 flex-shrink-0">
  % include(tpl + 'h1', h1=title + 'search')
  % include(tpl + 'navigation')
  <div class="card mb-3">
    <div class="card-body">
      <p class="card-text text-secondary">
        <form action="/search" method="GET">
          <div class="form-group">
            <input type="text" class="form-control" aria-describedby="tagsHelp"
            id="tags" name="tags">
            <small id="tagsHelp" class="form-text text-muted">
              Tags in lowercase (e.g., duck test)
            </small>
          </div>
          <button type="submit" class="btn btn-info" name="search" value="search">
            Search
          </button>
        </form>
      </p>
    </div>
  </div>
</main>
%include(tpl + 'footer')
%include(tpl + 'javascript')
</body>
</html>
