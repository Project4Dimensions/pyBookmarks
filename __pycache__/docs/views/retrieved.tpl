%# template to generate entries from SQL SELECT list
<!DOCTYPE html>
<html lang="en">
% include('docs/views/head', title='Retrieved')

<body>
<div class="container">
  % include('docs/views/h1', h1='Retrieved')
  % include('docs/views/navigation')
  %for row in rows:
    % include('docs/views/list', update_delete='1')
  %end
</div>
</body>
</html>
