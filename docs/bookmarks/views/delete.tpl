<!DOCTYPE html>
<html lang="en" class="h-100">
% include(tpl + 'head', title=title + 'delete')
<body class="d-flex flex-column h-100">
<main role="main" class="container mt-3 flex-shrink-0">
  % include(tpl + 'h1', h1=title + 'delete ')
  % include(tpl + 'navigation')
  % include(tpl + 'form', path=pth, title=old[0], uri=old[1], tags=old[2], note=old[3], name='delete_row', label='Delete')
</main>
%include(tpl + 'footer')
%include(tpl + 'javascript')
</body>
</html>
