<!DOCTYPE html>
<html lang="en" class="h-100">
% include(tpl + 'head', title=title + 'create')
<body class="d-flex flex-column h-100">
<main role="main" class="container mt-3 flex-shrink-0">
  % include(tpl + 'h1', h1=title + 'create')
  % include(tpl + 'form', path='/create', title='', uri='', tags='', note='', name='create', label='create')
</main>
%include(tpl + 'footer')
%include(tpl + 'javascript')
</body>
</html>
