/**
 * 流程串联：?flow=basic | ?flow=ai，localStorage 记忆，自动修正分支导航
 */
(function () {
  const params = new URLSearchParams(location.search);
  let flow = params.get('flow');
  if (flow === 'ai' || flow === 'basic') {
    localStorage.setItem('deom-flow', flow);
  } else {
    flow = localStorage.getItem('deom-flow') || 'basic';
  }

  const FLOWS = {
    basic: [
      { file: '01-login.html', label: '登录' },
      { file: '02-work-order-list.html', label: '选工单' },
      { file: '03-work-order-confirm.html', label: '确认作业' },
      { file: '04-inspection-preview-on.html', label: '预览开' },
      { file: '05-inspection-preview-off.html', label: '预览关' },
      { file: '06-photo-review.html', label: '照片回看' },
      { file: '07-upload-match-success.html', label: '上传留档' },
      { file: '09-upload-complete.html', label: '上传完成' },
      { file: '10-task-end.html', label: '结束任务' },
    ],
    ai: [
      { file: '01-login.html', label: '登录' },
      { file: '02-work-order-list.html', label: '选工单' },
      { file: '03-work-order-confirm-ai.html', label: '确认作业' },
      { file: '09-ai-hub.html', label: '能力菜单' },
      { file: '10-ai-fastener-count.html', label: '紧固件计数' },
      { file: '11-ai-cert-translate.html', label: '证书翻译' },
      { file: '12-ai-invoice-capture.html', label: '发票识别' },
      { file: '13-ai-data-entry.html', label: '数据入库' },
      { file: '14-task-complete.html', label: '结束任务' },
    ],
  };

  window.DEOM_FLOW = flow;

  function withFlow(href) {
    if (!href || href.startsWith('#') || href.startsWith('http')) return href;
    const base = href.split('?')[0];
    if (flow !== 'ai') return base;
    return base + '?flow=ai';
  }

  function currentFile() {
    return location.pathname.split('/').pop().split('?')[0];
  }

  /** 按当前页面所在目录计算 index 相对路径（与 flow 模式无关） */
  function indexHref() {
    const path = location.pathname.replace(/\\/g, '/');
    if (path.includes('/screens/ai/')) return '../../index.html';
    if (path.includes('/screens/')) return '../index.html';
    return 'index.html';
  }

  function renderFlowBar() {
    const steps = FLOWS[flow];
    if (!steps) return;

    const file = currentFile();
    let idx = steps.findIndex((s) => s.file === file);
    if (idx < 0) return;

    const bar = document.createElement('div');
    bar.className = 'flow-walkthrough flow-walkthrough--' + flow;
    bar.innerHTML =
      '<div class="flow-walkthrough__head">' +
      '<span class="flow-walkthrough__badge">' +
      (flow === 'ai' ? '增强版流程' : '基础版流程') +
      '</span>' +
      '<span class="flow-walkthrough__progress">步骤 ' +
      (idx + 1) +
      ' / ' +
      steps.length +
      '</span>' +
      '<a class="flow-walkthrough__home" href="' +
      indexHref() +
      '">流程总览</a>' +
      '</div>' +
      '<div class="flow-walkthrough__steps">' +
      steps
        .map(function (s, i) {
          var cls = 'flow-walkthrough__step';
          if (i === idx) cls += ' flow-walkthrough__step--active';
          else if (i < idx) cls += ' flow-walkthrough__step--done';
          return '<span class="' + cls + '">' + s.label + '</span>';
        })
        .join('<span class="flow-walkthrough__arrow">→</span>') +
      '</div>';
    document.body.insertBefore(bar, document.body.firstChild);
  }

  function applyNav() {
    document.querySelectorAll('.nav-btn[data-flow-ai-href]').forEach(function (a) {
      if (flow === 'ai') {
        a.setAttribute('href', withFlow(a.getAttribute('data-flow-ai-href')));
      } else {
        a.setAttribute('href', withFlow(a.getAttribute('href')));
      }
    });

    document.querySelectorAll('.nav-btn:not([data-flow-ai-href])').forEach(function (a) {
      var href = a.getAttribute('href');
      if (href && !href.includes('index.html')) {
        a.setAttribute('href', withFlow(href));
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    applyNav();
    renderFlowBar();
  });
})();
