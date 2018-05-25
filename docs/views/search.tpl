<!doctype html>
<html lang="en">
% include('docs/views/head', title='Search')

<body>
<div class="container">
  % include('docs/views/h1', h1='Search')
  % include('docs/views/navigation')
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
</div>
</body>
</html>
