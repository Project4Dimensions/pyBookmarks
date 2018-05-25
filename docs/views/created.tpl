<!DOCTYPE html>
<html lang="en">
% include('docs/views/head', title='Created bookmark')

<body>
<div class="container">
  % include('docs/views/h1', h1='Created bookmark')
  % include('docs/views/navigation')
  % include('docs/views/list', update_delete='1')
  % include('docs/views/action', action='Created bookmark', row_id=row_id)
</div>
</body>
</html>
