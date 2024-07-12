<!DOCTYPE html>
<html lang="en" class="h-100">
% include(tpl + 'head', title=title + 'start')
<body class="d-flex flex-column h-100">
<main role="main" class="container mt-3 flex-shrink-0">
  % include(tpl + 'h1', h1=title + 'start')
  <div class="card mb-3">
    <div class="card-body">
      <p class="card-text text-secondary">
        This web app creates, retrieves, updates, and deletes bookmark entries.
        It works with any <strong>modern web browser</strong>; see the
        <a href="https://browsehappy.com/" class="text-info">Browse Happy</a>
        website.
      </p>
      <p class="card-text text-secondary">
        Start by clicking on one of the navigation links labelled
        <strong>create, retrieve all, or search</strong>.
      </p>
    </div>
  </div>
</main>
%include(tpl + 'footer')
%include(tpl + 'javascript')
</body>
</html>
