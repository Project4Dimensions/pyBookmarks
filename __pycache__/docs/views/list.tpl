%# generate SQL SELECT list
  % id = row[0]
  % subject = row[1]
  % uri = row[2]
  % tags = row[3]
  % note = row[4].replace('\n', '<br>\n      ')
  <div class="card mb-3">
    <div class="card-body">
      <p class="card-text text-secondary">
        <span class="text-monospace">Subject&vellip;</span>
        {{subject}}<br>
        <span class="text-monospace">URI&nbsp;&vellip;</span>
        <a href="{{uri}}"  class="text-secondary">
          {{uri}}
        </a><br>
        <span class="text-monospace">Tags&vellip;</span>
        {{tags}}<br>
        <span class="text-monospace">Note&vellip;</span>
        {{!note}}
      </p>
      % if update_delete=='1':
      <p class="card-text text-secondary">
        <a href="/update/{{id}}" class="text-info">update</a> ·
        <a href="/delete/{{id}}" class="text-info">delete</a>
      </p>
      % end
    </div>
  </div>
