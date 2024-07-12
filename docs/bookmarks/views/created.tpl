<!DOCTYPE html>
<html lang="en" class="h-100">
% include(tpl + 'head', title=title + 'created bookmark')
<body class="d-flex flex-column h-100">
<main role="main" class="container mt-3 flex-shrink-0">
  % include(tpl + 'h1', h1=title + 'created bookmark')
  % include(tpl + 'list', update_delete='1')
  % include(tpl + 'action', action='Created bookmark', row_id=row_id)
</main>
%include(tpl + 'footer')
%include(tpl + 'javascript')
</body>
</html>
