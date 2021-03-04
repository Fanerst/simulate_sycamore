<!DOCTYPE html>
<html class="with-system-header with-system-footer" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<link as="style" href="https://code.itp.ac.cn/assets/application-bf1ba5d5d3395adc5bad6f17cc3cb21b3fb29d3e3471a5b260e0bc5ec7a57bc4.css" rel="preload">
<link as="style" href="https://code.itp.ac.cn/assets/highlight/themes/white-0678dba52a34ddc3b009cf294c54cfbddb9bac5991d6377ab811afe156e5a0cb.css" rel="preload">
<link as="font" href="https://code.itp.ac.cn/assets/fontawesome-webfont-2adefcbc041e7d18fcf2d417879dc5a09997aa64d675b7a3c4b6ce33da13f3fe.woff2?v=4.7.0" rel="preload" type="font/woff2">

<meta content="IE=edge" http-equiv="X-UA-Compatible">

<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py · refine · Feng Pan / sycamore20" property="og:title">
<meta content="Tensor network simulation of Sycamore circuit" property="og:description">
<meta content="https://code.itp.ac.cn/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://code.itp.ac.cn/panfeng/sycamore20/-/blob/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py · refine · Feng Pan / sycamore20" property="twitter:title">
<meta content="Tensor network simulation of Sycamore circuit" property="twitter:description">
<meta content="https://code.itp.ac.cn/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="twitter:image">

<title>BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py · refine · Feng Pan / sycamore20 · GitLab</title>
<meta content="Tensor network simulation of Sycamore circuit" name="description">
<link rel="shortcut icon" type="image/png" href="/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" id="favicon" data-original-href="/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" />

<link rel="stylesheet" media="all" href="/assets/application-bf1ba5d5d3395adc5bad6f17cc3cb21b3fb29d3e3471a5b260e0bc5ec7a57bc4.css" />

<link rel="stylesheet" media="all" href="/assets/application_utilities-4a0a7fb4b050255fc637b897e541f513df1cdf23cb1518fabc4323f2d0b78866.css" />
<link rel="stylesheet" media="all" href="/assets/themes/theme_indigo-1e3c170ae7fd24d137960957cba8221abf63a78f8b108e77f131b0fed6a659c7.css" />

<link rel="stylesheet" media="all" href="/assets/highlight/themes/white-0678dba52a34ddc3b009cf294c54cfbddb9bac5991d6377ab811afe156e5a0cb.css" />


<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://code.itp.ac.cn/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=15;gon.asset_host=null;gon.webpack_public_path="/assets/webpack/";gon.relative_url_root="";gon.shortcuts_path="/help/shortcuts";gon.user_color_scheme="white";gon.gitlab_url="https://code.itp.ac.cn";gon.revision="9cf4cc50386";gon.gitlab_logo="/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png";gon.sprite_icons="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg";gon.sprite_file_icons="/assets/file_icons-c13caf2f3ca00cc2c02b11d373ac288c200b9b4dcddbb52a5027dc07b3eece19.svg";gon.emoji_sprites_css_path="/assets/emoji_sprites-289eccffb1183c188b630297431be837765d9ff4aed6130cf738586fb307c170.css";gon.test_env=false;gon.disable_animations=null;gon.suggested_label_colors={"#0033CC":"UA blue","#428BCA":"Moderate blue","#44AD8E":"Lime green","#A8D695":"Feijoa","#5CB85C":"Slightly desaturated green","#69D100":"Bright green","#004E00":"Very dark lime green","#34495E":"Very dark desaturated blue","#7F8C8D":"Dark grayish cyan","#A295D6":"Slightly desaturated blue","#5843AD":"Dark moderate blue","#8E44AD":"Dark moderate violet","#FFECDB":"Very pale orange","#AD4363":"Dark moderate pink","#D10069":"Strong pink","#CC0033":"Strong red","#FF0000":"Pure red","#D9534F":"Soft red","#D1D100":"Strong yellow","#F0AD4E":"Soft orange","#AD8D43":"Dark moderate orange"};gon.first_day_of_week=1;gon.ee=false;gon.current_user_id=68;gon.current_username="panzhang";gon.current_user_fullname="Pan Zhang";gon.current_user_avatar_url="https://secure.gravatar.com/avatar/cb0cf6db13066aa46ac60d1918bd0dec?s=80\u0026d=identicon";gon.features={"webperfExperiment":false,"snippetsBinaryBlob":false,"usageDataApi":true,"securityAutoFix":false,"startupCss":false,"gitlabCiYmlPreview":false};gon.experiments={"suggestPipeline":false};
//]]>
</script>



<script src="/assets/webpack/runtime.754b8795.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.59a5d259.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-globalSearch-pages.admin.abuse_reports-pages.admin.groups.show-pages.admin.projects-pages.ad-c08b40ef.a8bba176.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.boards-pages.groups.details-pages.groups.show-pages.projects-pages.projects.act-5eeff683.eaa04149.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.admin.application_settings-pages.admin.application_settings.general-pages.admin.applic-5753b007.27b564d8.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.milestones.edit-pages.groups.milestones.new-pages.projects.blame.show-pages.pro-77e8c306.37c1e60d.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blame.show-pages.projects.blob.edit-pages.projects.blob.new-pages.projects.bl-c6edf1dd.8cdea721.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.shared.web_ide_link-pages.projects.show-pages.projec-cf300cc3.8162309e.chunk.js" defer="defer"></script>
<script src="/assets/webpack/pages.projects.blob.show.89c8d85e.chunk.js" defer="defer"></script>

<script>
//<![CDATA[
window.uploads_path = "/panfeng/sycamore20/uploads";



//]]>
</script>
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="1wBN22DjoWvgcq7lMTL0stogWO7Ky9vvYPsvLJUCw3+aagX81XZ03IyHnlRCeILT8H4BNkblf6URokUyrJxILA==" />
<meta name="csp-nonce" />
<meta name="action-cable-url" content="/-/cable" />
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<link color="rgb(226, 67, 41)" href="/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<meta content="/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">




</head>

<body class="ui-indigo tab-width-8  gl-browser-chrome gl-platform-mac" data-find-file="/panfeng/sycamore20/-/find_file/refine" data-namespace-id="121" data-page="projects:blob:show" data-page-type-id="refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py" data-project="sycamore20" data-project-id="663">

<script>
//<![CDATA[
gl = window.gl || {};
gl.client = {"isChrome":true,"isMac":true};


//]]>
</script>

<div class="header-message" style="background-color: #307df8;color: #ffffff"><p>Advanced Computing Platform for Theoretical Physics</p></div>
<header class="navbar navbar-gitlab navbar-expand-sm js-navbar" data-qa-selector="navbar">
<a class="sr-only gl-accessibility" href="#content-body" tabindex="1">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container">
<h1 class="title">
<span class="gl-sr-only">GitLab</span>
<a title="Dashboard" id="logo" href="/"><svg width="24" height="24" class="tanuki-logo" viewBox="0 0 36 36">
  <path class="tanuki-shape tanuki-left-ear" fill="#e24329" d="M2 14l9.38 9v-9l-4-12.28c-.205-.632-1.176-.632-1.38 0z"/>
  <path class="tanuki-shape tanuki-right-ear" fill="#e24329" d="M34 14l-9.38 9v-9l4-12.28c.205-.632 1.176-.632 1.38 0z"/>
  <path class="tanuki-shape tanuki-nose" fill="#e24329" d="M18,34.38 3,14 33,14 Z"/>
  <path class="tanuki-shape tanuki-left-eye" fill="#fc6d26" d="M18,34.38 11.38,14 2,14 6,25Z"/>
  <path class="tanuki-shape tanuki-right-eye" fill="#fc6d26" d="M18,34.38 24.62,14 34,14 30,25Z"/>
  <path class="tanuki-shape tanuki-left-cheek" fill="#fca326" d="M2 14L.1 20.16c-.18.565 0 1.2.5 1.56l17.42 12.66z"/>
  <path class="tanuki-shape tanuki-right-cheek" fill="#fca326" d="M34 14l1.9 6.16c.18.565 0 1.2-.5 1.56L18 34.38z"/>
</svg>

<span class="logo-text d-none d-lg-block gl-ml-3">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 617 169"><path d="M315.26 2.97h-21.8l.1 162.5h88.3v-20.1h-66.5l-.1-142.4M465.89 136.95c-5.5 5.7-14.6 11.4-27 11.4-16.6 0-23.3-8.2-23.3-18.9 0-16.1 11.2-23.8 35-23.8 4.5 0 11.7.5 15.4 1.2v30.1h-.1m-22.6-98.5c-17.6 0-33.8 6.2-46.4 16.7l7.7 13.4c8.9-5.2 19.8-10.4 35.5-10.4 17.9 0 25.8 9.2 25.8 24.6v7.9c-3.5-.7-10.7-1.2-15.1-1.2-38.2 0-57.6 13.4-57.6 41.4 0 25.1 15.4 37.7 38.7 37.7 15.7 0 30.8-7.2 36-18.9l4 15.9h15.4v-83.2c-.1-26.3-11.5-43.9-44-43.9M557.63 149.1c-8.2 0-15.4-1-20.8-3.5V70.5c7.4-6.2 16.6-10.7 28.3-10.7 21.1 0 29.2 14.9 29.2 39 0 34.2-13.1 50.3-36.7 50.3m9.2-110.6c-19.5 0-30 13.3-30 13.3v-21l-.1-27.8h-21.3l.1 158.5c10.7 4.5 25.3 6.9 41.2 6.9 40.7 0 60.3-26 60.3-70.9-.1-35.5-18.2-59-50.2-59M77.9 20.6c19.3 0 31.8 6.4 39.9 12.9l9.4-16.3C114.5 6 97.3 0 78.9 0 32.5 0 0 28.3 0 85.4c0 59.8 35.1 83.1 75.2 83.1 20.1 0 37.2-4.7 48.4-9.4l-.5-63.9V75.1H63.6v20.1h38l.5 48.5c-5 2.5-13.6 4.5-25.3 4.5-32.2 0-53.8-20.3-53.8-63-.1-43.5 22.2-64.6 54.9-64.6M231.43 2.95h-21.3l.1 27.3v94.3c0 26.3 11.4 43.9 43.9 43.9 4.5 0 8.9-.4 13.1-1.2v-19.1c-3.1.5-6.4.7-9.9.7-17.9 0-25.8-9.2-25.8-24.6v-65h35.7v-17.8h-35.7l-.1-38.5M155.96 165.47h21.3v-124h-21.3v124M155.96 24.37h21.3V3.07h-21.3v21.3"/></svg>

</span>
</a></h1>
<ul class="list-unstyled navbar-sub-nav">
<li id="nav-projects-dropdown" class="home dropdown header-projects qa-projects-dropdown" data-track-label="projects_dropdown" data-track-event="click_dropdown" data-track-value=""><button data-toggle="dropdown" type="button">
Projects
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-projects-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-projects-link" href="/dashboard/projects">Your projects
</a></li><li class=""><a href="/dashboard/projects/starred">Starred projects
</a></li><li class=""><a href="/explore">Explore projects
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-project-id="663" data-project-name="sycamore20" data-project-namespace="Feng Pan / sycamore20" data-project-web-url="/panfeng/sycamore20" data-user-name="panzhang" id="js-projects-dropdown"></div>
</div>
</div>

</div>
</li><li id="nav-groups-dropdown" class="d-none d-md-block home dropdown header-groups qa-groups-dropdown" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><button data-toggle="dropdown" type="button">
Groups
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-groups-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-groups-link" href="/dashboard/groups">Your groups
</a></li><li class=""><a href="/explore/groups">Explore groups
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-user-name="panzhang" id="js-groups-dropdown"></div>
</div>
</div>

</div>
</li><li class="header-more dropdown">
<a data-qa-selector="more_dropdown" data-toggle="dropdown" href="#">
More
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</a>
<div class="dropdown-menu">
<ul>
<li class="d-md-none">
<a class="dashboard-shortcuts-groups" data-qa-selector="groups_link" href="/dashboard/groups">Groups
</a></li>
<li class=""><a class="dashboard-shortcuts-activity" data-qa-selector="activity_link" href="/dashboard/activity">Activity
</a></li><li class=""><a class="dashboard-shortcuts-milestones" data-qa-selector="milestones_link" href="/dashboard/milestones">Milestones
</a></li><li class=""><a class="dashboard-shortcuts-snippets" data-qa-selector="snippets_link" href="/dashboard/snippets">Snippets
</a></li><li class="dropdown">

</li>
<li class=""><a class="admin-icon qa-admin-area-link d-xl-none" href="/admin">Admin Area
</a></li></ul>
</div>
</li>
<li class="d-none d-xl-block"><a class="admin-icon qa-admin-area-link" title="Admin Area" aria-label="Admin Area" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/admin"><svg class="s18" data-testid="admin-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#admin"></use></svg>
</a></li><li class="hidden">
<a class="dashboard-shortcuts-projects" href="/dashboard/projects">Projects
</a></li>

</ul>

</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="header-new dropdown" data-track-event="click_dropdown" data-track-label="new_dropdown" data-track-value="">
<a class="header-new-dropdown-toggle has-tooltip qa-new-menu-toggle" id="js-onboarding-new-project-link" title="New..." ref="tooltip" aria-label="New..." data-toggle="dropdown" data-placement="bottom" data-container="body" data-display="static" href="/projects/new"><svg class="s16" data-testid="plus-square-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#plus-square"></use></svg>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="dropdown-bold-header">
This project
</li>
<li><a href="/panfeng/sycamore20/-/issues/new">New issue</a></li>
<li><a href="/panfeng/sycamore20/-/merge_requests/new">New merge request</a></li>
<li><a href="/panfeng/sycamore20/-/snippets/new">New snippet</a></li>
<li class="divider"></li>
<li class="dropdown-bold-header">GitLab</li>
<li><a class="qa-global-new-project-link" href="/projects/new">New project</a></li>
<li><a href="/groups/new">New group</a></li>
<li><a class="qa-global-new-snippet-link" href="/-/snippets/new">New snippet</a></li>
</ul>
</div>
</li>

<li class="nav-item d-none d-lg-block m-auto">
<div class="search search-form" data-track-event="activate_form_input" data-track-label="navbar_search" data-track-value="">
<form class="form-inline" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><div class="search-input-container">
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search or jump to…" class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options" spellcheck="false" tabindex="1" autocomplete="off" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" data-qa-selector="search_term_field" aria-label="Search or jump to…" />
<button class="hidden js-dropdown-search-toggle" data-toggle="dropdown" type="button"></button>
<div class="dropdown-menu dropdown-select js-dashboard-search-options">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
<svg class="s16 search-icon" data-testid="search-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#search"></use></svg>
<svg class="s16 clear-icon js-clear-input" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" value="" class="js-search-group-options" />
<input type="hidden" name="project_id" id="search_project_id" value="663" class="js-search-project-options" data-project-path="sycamore20" data-name="sycamore20" data-issues-path="/panfeng/sycamore20/-/issues" data-mr-path="/panfeng/sycamore20/-/merge_requests" data-issues-disabled="false" />
<input type="hidden" name="scope" id="scope" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="snippets" id="snippets" value="false" />
<input type="hidden" name="repository_ref" id="repository_ref" value="refine" />
<input type="hidden" name="nav_source" id="nav_source" value="navbar" />
<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="663" data-autocomplete-project-ref="refine"></div>
</form></div>

</li>
<li class="nav-item d-inline-block d-lg-none">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search?project_id=663"><svg class="s16" data-testid="search-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#search"></use></svg>
</a></li>
<li class="user-counter"><a title="Issues" class="dashboard-shortcuts-issues" aria-label="Issues" data-qa-selector="issues_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_issues_link" data-track-property="navigation" data-container="body" href="/dashboard/issues?assignee_username=panzhang"><svg class="s16" data-testid="issues-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#issues"></use></svg>
<span class="badge badge-pill green-badge hidden issues-count">
0
</span>
</a></li><li class="user-counter"><a title="Merge requests" class="dashboard-shortcuts-merge_requests" aria-label="Merge requests" data-qa-selector="merge_requests_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_merge_link" data-track-property="navigation" data-container="body" href="/dashboard/merge_requests?assignee_username=panzhang"><svg class="s16" data-testid="git-merge-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#git-merge"></use></svg>
<span class="badge badge-pill hidden merge-requests-count">
0
</span>
</a></li><li class="user-counter"><a title="To-Do List" aria-label="To-Do List" class="shortcuts-todos" data-qa-selector="todos_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_to_do_link" data-track-property="navigation" data-container="body" href="/dashboard/todos"><svg class="s16" data-testid="todo-done-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#todo-done"></use></svg>
<span class="badge badge-pill hidden js-todos-count todos-count">
0
</span>
</a></li><li class="nav-item header-help dropdown d-none d-md-block">
<a class="header-help-dropdown-toggle" data-toggle="dropdown" href="/help"><span class="gl-sr-only">
Help
</span>
<svg class="s16" data-testid="question-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#question"></use></svg>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>

<li>
<a href="/help">Help</a>
</li>
<li>
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li>
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-event="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com/">Community forum</a>

</li>
<li>
<button class="js-shortcuts-modal-trigger" type="button">
Keyboard shortcuts
<span aria-hidden class="text-secondary float-right">?</span>
</button>
</li>
<li class="divider"></li>
<li>
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li>
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>
</li>
<li class="divider"></li>
<li>
<a target="_blank" class="text-nowrap" href="/admin/instance_review">Get a free instance review
</a></li>

</ul>

</div>
</li>
<li class="dropdown header-user js-nav-user-dropdown nav-item" data-qa-selector="user_menu" data-track-event="click_dropdown" data-track-label="profile_dropdown" data-track-value="">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="/panzhang"><img width="23" height="23" class="header-user-avatar qa-user-avatar lazy" alt="Pan Zhang" data-src="https://secure.gravatar.com/avatar/cb0cf6db13066aa46ac60d1918bd0dec?s=46&amp;d=identicon" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />

<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="current-user">
<div class="user-name bold">
Pan Zhang
</div>
@panzhang
</li>
<li class="divider"></li>
<li>
<button class="btn menu-item js-set-status-modal-trigger" type="button">
Set status
</button>
</li>
<li>
<a class="profile-link" data-user="panzhang" href="/panzhang">Profile</a>
</li>
<li>
<a data-qa-selector="settings_link" href="/profile">Settings</a>
</li>


<li class="divider d-md-none"></li>
<li class="d-md-none">
<a href="/help">Help</a>
</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li class="d-md-none">
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-event="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com/">Community forum</a>

</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li class="d-md-none">
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>
</li>
<li class="divider"></li>
<li>
<a target="_blank" class="text-nowrap" href="/admin/instance_review">Get a free instance review
</a></li>

<li class="divider"></li>
<li>
<a class="sign-out-link" data-qa-selector="sign_out_link" rel="nofollow" data-method="post" href="/users/sign_out">Sign out</a>
</li>
</ul>

</div>
</li>
</ul>
</div>
<button class="navbar-toggler d-block d-sm-none" type="button">
<span class="sr-only">Toggle navigation</span>
<svg class="s12 more-icon js-navbar-toggle-right" data-testid="ellipsis_h-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#ellipsis_h"></use></svg>
<svg class="s12 close-icon js-navbar-toggle-left" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg>
</button>
</div>
</div>
</header>
<div class="js-set-status-modal-wrapper" data-current-emoji="" data-current-message=""></div>

<div class="layout-page page-with-contextual-sidebar">
<div class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<div class="context-header">
<a title="sycamore20" href="/panfeng/sycamore20"><div class="avatar-container rect-avatar s40 project-avatar">
<div class="avatar s40 avatar-tile identicon bg6">S</div>
</div>
<div class="sidebar-context-title">
sycamore20
</div>
</a></div>
<ul class="sidebar-top-level-items qa-project-sidebar">
<li class="home"><a class="shortcuts-project rspec-project-link" data-qa-selector="project_link" href="/panfeng/sycamore20"><div class="nav-icon-container">
<svg class="s16" data-testid="home-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#home"></use></svg>
</div>
<span class="nav-item-name">
Project overview
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20"><strong class="fly-out-top-item-name">
Project overview
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Project details" class="shortcuts-project" href="/panfeng/sycamore20"><span>Details</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" data-qa-selector="activity_link" href="/panfeng/sycamore20/activity"><span>Activity</span>
</a></li><li class=""><a title="Releases" class="shortcuts-project-releases" href="/panfeng/sycamore20/-/releases"><span>Releases</span>
</a></li></ul>
</li><li class="active"><a class="shortcuts-tree" data-qa-selector="repository_link" href="/panfeng/sycamore20/-/tree/refine"><div class="nav-icon-container">
<svg class="s16" data-testid="doc-text-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#doc-text"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-repo-link">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><a href="/panfeng/sycamore20/-/tree/refine"><strong class="fly-out-top-item-name">
Repository
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class="active"><a href="/panfeng/sycamore20/-/tree/refine">Files
</a></li><li class=""><a id="js-onboarding-commits-link" href="/panfeng/sycamore20/-/commits/refine">Commits
</a></li><li class=""><a data-qa-selector="branches_link" id="js-onboarding-branches-link" href="/panfeng/sycamore20/-/branches">Branches
</a></li><li class=""><a data-qa-selector="tags_link" href="/panfeng/sycamore20/-/tags">Tags
</a></li><li class=""><a href="/panfeng/sycamore20/-/graphs/refine">Contributors
</a></li><li class=""><a href="/panfeng/sycamore20/-/network/refine">Graph
</a></li><li class=""><a href="/panfeng/sycamore20/-/compare?from=master&amp;to=refine">Compare
</a></li>
</ul>
</li><li class=""><a class="shortcuts-issues qa-issues-item" href="/panfeng/sycamore20/-/issues"><div class="nav-icon-container">
<svg class="s16" data-testid="issues-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#issues"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-issues-link">
Issues
</span>
<span class="badge badge-pill count issue_counter">
0
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/issues"><strong class="fly-out-top-item-name">
Issues
</strong>
<span class="badge badge-pill count issue_counter fly-out-badge">
0
</span>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Issues" href="/panfeng/sycamore20/-/issues"><span>
List
</span>
</a></li><li class=""><a title="Boards" data-qa-selector="issue_boards_link" href="/panfeng/sycamore20/-/boards"><span>
Boards
</span>
</a></li><li class=""><a title="Labels" class="qa-labels-link" href="/panfeng/sycamore20/-/labels"><span>
Labels
</span>
</a></li><li class=""><a title="Service Desk" href="/panfeng/sycamore20/-/issues/service_desk">Service Desk
</a></li>
<li class=""><a title="Milestones" class="qa-milestones-link" href="/panfeng/sycamore20/-/milestones"><span>
Milestones
</span>
</a></li>
</ul>
</li><li class=""><a class="shortcuts-merge_requests" data-qa-selector="merge_requests_link" href="/panfeng/sycamore20/-/merge_requests"><div class="nav-icon-container">
<svg class="s16" data-testid="git-merge-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#git-merge"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-mr-link">
Merge Requests
</span>
<span class="badge badge-pill count merge_counter js-merge-counter">
0
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/merge_requests"><strong class="fly-out-top-item-name">
Merge Requests
</strong>
<span class="badge badge-pill count merge_counter js-merge-counter fly-out-badge">
0
</span>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-pipelines qa-link-pipelines rspec-link-pipelines" data-qa-selector="ci_cd_link" href="/panfeng/sycamore20/-/pipelines"><div class="nav-icon-container">
<svg class="s16" data-testid="rocket-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#rocket"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-pipelines-link">
CI / CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/pipelines"><strong class="fly-out-top-item-name">
CI / CD
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Pipelines" class="shortcuts-pipelines" href="/panfeng/sycamore20/-/pipelines"><span>
Pipelines
</span>
</a></li><li class=""><a title="Jobs" class="shortcuts-builds" href="/panfeng/sycamore20/-/jobs"><span>
Jobs
</span>
</a></li><li class=""><a title="Schedules" class="shortcuts-builds" href="/panfeng/sycamore20/-/pipeline_schedules"><span>
Schedules
</span>
</a></li>
</ul>
</li>
<li class=""><a class="shortcuts-operations" data-qa-selector="operations_link" href="/panfeng/sycamore20/-/environments/metrics"><div class="nav-icon-container">
<svg class="s16" data-testid="cloud-gear-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#cloud-gear"></use></svg>
</div>
<span class="nav-item-name">
Operations
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/environments/metrics"><strong class="fly-out-top-item-name">
Operations
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Metrics" class="shortcuts-metrics" data-qa-selector="operations_metrics_link" href="/panfeng/sycamore20/-/metrics"><span>
Metrics
</span>
</a></li><li class=""><a title="Logs" href="/panfeng/sycamore20/-/logs"><span>
Logs
</span>
</a></li><li class=""><a title="Tracing" href="/panfeng/sycamore20/-/tracing"><span>
Tracing
</span>
</a></li>
<li class=""><a title="Error Tracking" href="/panfeng/sycamore20/-/error_tracking"><span>
Error Tracking
</span>
</a></li><li class=""><a title="Alerts" href="/panfeng/sycamore20/-/alert_management"><span>
Alerts
</span>
</a></li><li class=""><a title="Incidents" data-qa-selector="operations_incidents_link" href="/panfeng/sycamore20/-/incidents"><span>
Incidents
</span>
</a></li><li class=""><a title="Serverless" href="/panfeng/sycamore20/-/serverless/functions"><span>
Serverless
</span>
</a></li><li class=""><a title="Kubernetes" class="shortcuts-kubernetes" href="/panfeng/sycamore20/-/clusters"><span>
Kubernetes
</span>
</a></li><li class=""><a title="Environments" class="shortcuts-environments qa-operations-environments-link" href="/panfeng/sycamore20/-/environments"><span>
Environments
</span>
</a></li><li class=""><a title="Feature Flags" class="shortcuts-feature-flags" href="/panfeng/sycamore20/-/feature_flags"><span>
Feature Flags
</span>
</a></li></ul>
</li><li class=""><a data-qa-selector="packages_link" href="/panfeng/sycamore20/-/packages"><div class="nav-icon-container">
<svg class="s16" data-testid="package-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#package"></use></svg>
</div>
<span class="nav-item-name">
Packages &amp; Registries
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/packages"><strong class="fly-out-top-item-name">
Packages &amp; Registries
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Package Registry" href="/panfeng/sycamore20/-/packages"><span>Package Registry</span>
</a></li></ul>
</li>
<li class=""><a data-qa-selector="analytics_anchor" href="/panfeng/sycamore20/-/value_stream_analytics"><div class="nav-icon-container">
<svg class="s16" data-testid="chart-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chart"></use></svg>
</div>
<span class="nav-item-name" data-qa-selector="analytics_link">
Analytics
</span>
</a><ul class="sidebar-sub-level-items" data-qa-selector="analytics_sidebar_submenu">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/value_stream_analytics"><strong class="fly-out-top-item-name">
Analytics
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="CI / CD" href="/panfeng/sycamore20/-/pipelines/charts"><span>CI / CD</span>
</a></li><li class=""><a class="shortcuts-repository-charts" title="Repository" href="/panfeng/sycamore20/-/graphs/refine/charts"><span>Repository</span>
</a></li><li class=""><a class="shortcuts-project-cycle-analytics" title="Value Stream" href="/panfeng/sycamore20/-/value_stream_analytics"><span>Value Stream</span>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-wiki" data-qa-selector="wiki_link" href="/panfeng/sycamore20/-/wikis/home"><div class="nav-icon-container">
<svg class="s16" data-testid="book-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#book"></use></svg>
</div>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/wikis/home"><strong class="fly-out-top-item-name">
Wiki
</strong>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-snippets" data-qa-selector="snippets_link" href="/panfeng/sycamore20/-/snippets"><div class="nav-icon-container">
<svg class="s16" data-testid="snippet-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#snippet"></use></svg>
</div>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/snippets"><strong class="fly-out-top-item-name">
Snippets
</strong>
</a></li></ul>
</li><li class=""><a title="Members" class="qa-members-link" id="js-onboarding-members-link" href="/panfeng/sycamore20/-/project_members"><div class="nav-icon-container">
<svg class="s16" data-testid="users-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#users"></use></svg>
</div>
<span class="nav-item-name">
Members
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/-/project_members"><strong class="fly-out-top-item-name">
Members
</strong>
</a></li></ul>
</li><li class=""><a href="/panfeng/sycamore20/edit"><div class="nav-icon-container">
<svg class="s16" data-testid="settings-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#settings"></use></svg>
</div>
<span class="nav-item-name qa-settings-item" id="js-onboarding-settings-link">
Settings
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/panfeng/sycamore20/edit"><strong class="fly-out-top-item-name">
Settings
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="General" class="qa-general-settings-link" href="/panfeng/sycamore20/edit"><span>
General
</span>
</a></li><li class=""><a title="Integrations" data-qa-selector="integrations_settings_link" href="/panfeng/sycamore20/-/settings/integrations"><span>
Integrations
</span>
</a></li><li class=""><a title="Webhooks" data-qa-selector="webhooks_settings_link" href="/panfeng/sycamore20/hooks"><span>
Webhooks
</span>
</a></li><li class=""><a title="Access Tokens" data-qa-selector="access_tokens_settings_link" href="/panfeng/sycamore20/-/settings/access_tokens"><span>
Access Tokens
</span>
</a></li><li class=""><a title="Repository" href="/panfeng/sycamore20/-/settings/repository"><span>
Repository
</span>
</a></li><li class=""><a title="CI / CD" href="/panfeng/sycamore20/-/settings/ci_cd"><span>
CI / CD
</span>
</a></li><li class=""><a title="Operations" data-qa-selector="operations_settings_link" href="/panfeng/sycamore20/-/settings/operations">Operations
</a></li>
</ul>
</li><a class="toggle-sidebar-button js-toggle-sidebar qa-toggle-sidebar rspec-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class="s16 icon-chevron-double-lg-left" data-testid="chevron-double-lg-left-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-double-lg-left"></use></svg>
<svg class="s16 icon-chevron-double-lg-right" data-testid="chevron-double-lg-right-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-double-lg-right"></use></svg>
<span class="collapse-text">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg>
<span class="collapse-text">Close sidebar</span>
</button>
<li class="hidden">
<a title="Activity" class="shortcuts-project-activity" href="/panfeng/sycamore20/activity"><span>
Activity
</span>
</a></li>
<li class="hidden">
<a title="Network" class="shortcuts-network" href="/panfeng/sycamore20/-/network/refine">Graph
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="/panfeng/sycamore20/-/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a title="Jobs" class="shortcuts-builds" href="/panfeng/sycamore20/-/jobs">Jobs
</a></li>
<li class="hidden">
<a title="Commits" class="shortcuts-commits" href="/panfeng/sycamore20/-/commits/refine">Commits
</a></li>
<li class="hidden">
<a title="Issue Boards" class="shortcuts-issue-boards" href="/panfeng/sycamore20/-/boards">Issue Boards</a>
</li>
</ul>
</div>
</div>

<div class="content-wrapper">
<div class="mobile-overlay"></div>

<div class="alert-wrapper">













<nav class="breadcrumbs container-fluid container-limited" role="navigation">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">Open sidebar</span>
<svg class="s16" data-testid="hamburger-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#hamburger"></use></svg>
</button><div class="breadcrumbs-links js-title-container" data-qa-selector="breadcrumb_links_content">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a href="/panfeng">Feng Pan</a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#angle-right"></use></svg></li> <li><a href="/panfeng/sycamore20"><span class="breadcrumb-item-text js-breadcrumb-item-text">sycamore20</span></a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#angle-right"></use></svg></li>

<li>
<h2 class="breadcrumbs-sub-title"><a href="/panfeng/sycamore20/-/blob/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py">Repository</a></h2>
</li>
</ul>
</div>

</div>
</nav>

</div>
<div class="container-fluid container-limited ">
<div class="content" id="content-body">
<div class="flash-container flash-container-page sticky">
</div>

<div class="js-signature-container" data-signatures-path="/panfeng/sycamore20/-/commits/cd4c0eb9d6e0d9f6712b8912c622a3efd8a53ba2/signatures?limit=1"></div>

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/panfeng/sycamore20/-/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown qa-branches-select" type="button" data-toggle="dropdown" data-selected="refine" data-ref="refine" data-refs-url="/panfeng/sycamore20/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true"><span class="dropdown-toggle-text ">refine</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button>
<div class="dropdown-menu dropdown-menu-paging dropdown-menu-selectable git-revision-dropdown qa-branches-dropdown">
<div class="dropdown-page-one">
<div class="dropdown-title gl-display-flex"><span class="gl-ml-auto">Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close gl-ml-auto" aria-label="Close" type="button"><svg class="s16 dropdown-menu-close-icon" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field qa-dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><svg class="s16 dropdown-input-search" data-testid="search-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/panfeng/sycamore20/-/tree/refine">sycamore20
</a></li>
<li class="breadcrumb-item">
<a href="/panfeng/sycamore20/-/tree/refine/BipartitionBatch">BipartitionBatch</a>
</li>
<li class="breadcrumb-item">
<a href="/panfeng/sycamore20/-/tree/refine/BipartitionBatch/loadtensor">loadtensor</a>
</li>
<li class="breadcrumb-item">
<a href="/panfeng/sycamore20/-/tree/refine/BipartitionBatch/loadtensor/Sycamore">Sycamore</a>
</li>
<li class="breadcrumb-item">
<a href="/panfeng/sycamore20/-/blob/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py"><strong>circuit_n53_m20_s0_e0_pABCDCDAB.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-children-ml-sm-3"><a class="btn shortcuts-find-file" rel="nofollow" href="/panfeng/sycamore20/-/find_file/refine">Find file
</a><a class="btn js-blob-blame-link" href="/panfeng/sycamore20/-/blame/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py">Blame</a><a class="btn" href="/panfeng/sycamore20/-/commits/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py">History</a><a class="btn js-data-file-blob-permalink-url" href="/panfeng/sycamore20/-/blob/6783fa2f2dcfaf172c4eb5fd066887bbb2c6062a/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py">Permalink</a></div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-cd4c0eb9">
<div class="avatar-cell d-none d-sm-block">
<a href="mailto:fan_physics@126.com"><img alt="panfeng&#39;s avatar" src="https://secure.gravatar.com/avatar/cfabda26883a721005264f9c934aa71b?s=80&amp;d=identicon" class="avatar s40 d-none d-sm-inline-block" title="panfeng" /></a>
</div>
<div class="commit-detail flex-list">
<div class="commit-content qa-commit-content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/panfeng/sycamore20/-/commit/cd4c0eb9d6e0d9f6712b8912c622a3efd8a53ba2">init</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
cd4c0eb9
</span>
<div class="committer">
<a class="commit-author-link" href="mailto:fan_physics@126.com">panfeng</a> authored <time class="js-timeago" title="Jan 22, 2021 7:40am" datetime="2021-01-22T07:40:38Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Jan 22, 2021</time>
</div>

</div>
<div class="commit-actions flex-row">

<div class="js-commit-pipeline-status" data-endpoint="/panfeng/sycamore20/-/commit/cd4c0eb9d6e0d9f6712b8912c622a3efd8a53ba2/pipelines?ref=refine"></div>
<div class="commit-sha-group d-none d-sm-flex">
<div class="label label-monospace monospace">
cd4c0eb9
</div>
<button class="btn btn btn-default" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA" data-class="btn btn-default" data-clipboard-text="cd4c0eb9d6e0d9f6712b8912c622a3efd8a53ba2" type="button" title="Copy commit SHA" aria-label="Copy commit SHA"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#copy-to-clipboard"></use></svg></button>

</div>
</div>
</div>
</li>

</ul>
</div>


</div>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="js-file-title file-title-flex-parent">
<div class="file-header-content">
<svg class="s16" data-testid="doc-text-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#doc-text"></use></svg>
<strong class="file-title-name">
circuit_n53_m20_s0_e0_pABCDCDAB.py
</strong>
<button class="btn btn-clipboard btn-transparent" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn-clipboard btn-transparent" data-title="Copy file path" data-clipboard-text="{&quot;text&quot;:&quot;BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py&quot;,&quot;gfm&quot;:&quot;`BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py`&quot;}" type="button" title="Copy file path" aria-label="Copy file path"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#copy-to-clipboard"></use></svg></button>
<small class="mr-1">
256 KB
</small>
</div>

<div class="file-actions"><a class="btn btn-primary js-edit-blob ml-2  btn-sm" data-track-event="click_edit" data-track-label="Edit" href="/panfeng/sycamore20/-/edit/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py">Edit</a><a class="btn btn-primary ide-edit-button ml-2 btn-inverted btn-sm" data-track-event="click_edit_ide" data-track-label="Web IDE" data-track-property="secondary" href="/-/ide/project/panfeng/sycamore20/edit/refine/-/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py">Web IDE</a><div class="btn-group ml-2" role="group">

<button name="button" type="submit" class="btn btn-default" data-target="#modal-upload-blob" data-toggle="modal">Replace</button>
<button name="button" type="submit" class="btn btn-default" data-target="#modal-remove-blob" data-toggle="modal">Delete</button>
</div><div class="btn-group ml-2" role="group">
<button class="btn btn btn-sm js-copy-blob-source-btn" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn btn-sm js-copy-blob-source-btn" data-title="Copy file contents" data-clipboard-target=".blob-content[data-blob-id=&#39;95f99a0da5847e1fdfc1d767e99b8ff099f5a153&#39;]" type="button" title="Copy file contents" aria-label="Copy file contents"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#copy-to-clipboard"></use></svg></button>
<a class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" aria-label="Open raw" title="Open raw" data-container="body" href="/panfeng/sycamore20/-/raw/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py"><svg class="s16" data-testid="doc-code-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#doc-code"></use></svg></a>
<a download="BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py" class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" aria-label="Download" title="Download" data-container="body" href="/panfeng/sycamore20/-/raw/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py?inline=false"><svg class="s16" data-testid="download-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#download"></use></svg></a>

</div></div>
</div>
<div class="js-file-fork-suggestion-section file-fork-suggestion hidden">
<span class="file-fork-suggestion-note">
You're not allowed to
<span class="js-file-fork-suggestion-section-action">
edit
</span>
files in this project directly. Please fork this project,
make your changes there, and submit a merge request.
</span>
<a class="js-fork-suggestion-button btn btn-grouped btn-inverted btn-success" rel="nofollow" data-method="post" href="/panfeng/sycamore20/-/blob/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py">Fork</a>
<button class="js-cancel-fork-suggestion-button btn btn-grouped" type="button">
Cancel
</button>
</div>



<div data-blob-data="import cirq
import numpy as np

QUBIT_ORDER = [
    cirq.GridQubit(0, 5),
    cirq.GridQubit(0, 6),
    cirq.GridQubit(1, 4),
    cirq.GridQubit(1, 5),
    cirq.GridQubit(1, 6),
    cirq.GridQubit(1, 7),
    cirq.GridQubit(2, 4),
    cirq.GridQubit(2, 5),
    cirq.GridQubit(2, 6),
    cirq.GridQubit(2, 7),
    cirq.GridQubit(2, 8),
    cirq.GridQubit(3, 2),
    cirq.GridQubit(3, 3),
    cirq.GridQubit(3, 4),
    cirq.GridQubit(3, 5),
    cirq.GridQubit(3, 6),
    cirq.GridQubit(3, 7),
    cirq.GridQubit(3, 8),
    cirq.GridQubit(3, 9),
    cirq.GridQubit(4, 1),
    cirq.GridQubit(4, 2),
    cirq.GridQubit(4, 3),
    cirq.GridQubit(4, 4),
    cirq.GridQubit(4, 5),
    cirq.GridQubit(4, 6),
    cirq.GridQubit(4, 7),
    cirq.GridQubit(4, 8),
    cirq.GridQubit(4, 9),
    cirq.GridQubit(5, 0),
    cirq.GridQubit(5, 1),
    cirq.GridQubit(5, 2),
    cirq.GridQubit(5, 3),
    cirq.GridQubit(5, 4),
    cirq.GridQubit(5, 5),
    cirq.GridQubit(5, 6),
    cirq.GridQubit(5, 7),
    cirq.GridQubit(5, 8),
    cirq.GridQubit(6, 1),
    cirq.GridQubit(6, 2),
    cirq.GridQubit(6, 3),
    cirq.GridQubit(6, 4),
    cirq.GridQubit(6, 5),
    cirq.GridQubit(6, 6),
    cirq.GridQubit(6, 7),
    cirq.GridQubit(7, 2),
    cirq.GridQubit(7, 3),
    cirq.GridQubit(7, 4),
    cirq.GridQubit(7, 5),
    cirq.GridQubit(7, 6),
    cirq.GridQubit(8, 3),
    cirq.GridQubit(8, 4),
    cirq.GridQubit(8, 5),
    cirq.GridQubit(9, 4)
]

CIRCUIT = cirq.Circuit(moments=[
    cirq.Moment(operations=[
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 0)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.7743385483953005).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.7085204779284944).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.8687711187158653).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.3853766657859231).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.3522159558487364).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.569527381436443).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.06748036788071975).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.03542260032736748).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.921123478965347).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.940605149780575).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.40878079457469985).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.3573777822597026).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.4286328898578044).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.567173927172081).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.6962362636582926).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.6243336356713873).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.5070267688233168).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.49025706927611445).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.82479487914479).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.831505604695568).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.7654710267272109).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.7622667609489339).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.7530995459405583).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.7063901684965722).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.7750964509509387).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.9619956872914577).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.8310454946335954).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.8149432193242095).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.568448771120722).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.5458328527656618).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.46444025457872556).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.8641681946768033).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.33639050361710615).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.4121311900075394).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.881176970884841).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.8199816956867351).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.5174631371535426).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.5093922035705379).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.2684453761112637).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.26751780455859997).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.7883616255904944).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.9304903862480522).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.5471409474788239).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.5891117186780521).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.7384907660505857).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.7451407522809496).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * -0.1830293948567971).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.1757017537984857).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
            cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
            cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
            cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
            cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)),
        cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)),
        cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)),
        cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)),
        cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.7618064157555159).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.827624486222322).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.677790595837605).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.8388149512324528).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.34915411632258214).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.13184269073487556).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.4610625765182105).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.4290048089648583).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.6641998401797986).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.6836815109950266).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.026240452181357746).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.025162560133639312).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.9071761579568303).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.9542828047288932).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.46145806100291004).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.5333606889898155).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.5128100748460089).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.4960403752988061).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.5829645187562967).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.5762537932055181).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.022811401598836913).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.019607135820559906).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.8523020333228131).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.8990114107667992).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.9352866185158868).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.7483873821753678).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.9220101925888569).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.9059079172794712).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.7039221690166656).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.6813062506616053).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.6965073865506469).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.9037646733512754).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.45310524873049973).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.3773645623400665).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.42017342300456634).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.3589781478064599).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.9534707755965702).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.9615417091795746).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * 0.5368636250628501).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.5377911966155139).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.5123942238917779).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.7935422120532315).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.7898684772427236).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.7478977060434954).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.8571455144841159).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.8504955282537521).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.9094649565590708).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * 0.7318038947856463).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.Y**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.07221640979880403).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.17734365608174887).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.7166427083722222).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.717673588252228).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.1312926423470736).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.13158529074665537).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.7500367576549269).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.31797150857789674).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.8756735306896725).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.9327732133062662).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.7071565092929694).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.6264998637477406).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.82790347048799).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.8594778743809006).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.8064559428449068).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.7629602352736249).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.23630732076940514).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.25438180016733336).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.6476084230939583).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.6528339440806201).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.20879565669998532).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.26053049452558324).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.7777343640360711).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.8805385932920736).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.5137630264839785).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.48179097076948874).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.7693840211762448).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.7680082232923118).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.14188452450562264).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.1339396318115881).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.95616894502165).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.9015807139989003).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.3168365530459615).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.2898226701533191).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.32361247881294825).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.27931184143712456).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.884543382731205).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.8540367322639986).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)),
        cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.10267615219883607).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.14688391368171685).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.5303948572093229).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.529363977329317).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.6623304931849363).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.6626231415845181).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.06783382350879162).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.36423142556823856).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.9730909692986618).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.8353557746972768).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.5361169534193021).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.6167735989645307).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.6122117071342573).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.5806373032413467).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.968052322606287).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.9245566150350051).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.6534917441628949).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.6715662235608231).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.7407238202696524).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.7354982992829906).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.06340668623729523).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.40591946498827336).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.4557556128718794).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.558559842127882).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.923796560084577).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.9557686157990668).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.6313087990584325).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.6299330011745).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.20274234705300925).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.21068723974704434).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.5124187849542257).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.3701684439747759).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.3038733131602001).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.2768594302675577).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.26284256852387516).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.3071432058996983).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.7502523839911145).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.719745733523908).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.X**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 0)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.868874517623681).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * -0.5062300204223075).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.6874509025876478).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.6826684237245009).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.3757979651191995).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.3369000264078134).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.5165579149683887).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.9838406309684837).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.6517543596020707).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.8938908007211287).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.011576333256837757).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.1994965304792813).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.5357402786793479).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.5797224477448737).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.6015756389470484).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.573317645438219).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.3791786031325414).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.676931394322152).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.6257613274555152).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.6210571332355261).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.45193657844083596).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.16633011275543763).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.8632357323678501).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.5580904452638696).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.7226189706701976).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.7708292466716248).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.628899885711077).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * 0.8564821803203452).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.48600051750832335).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.40704671139578114).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.7509923227943213).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.7705635810307807).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.5247429096711106).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.31560248875795377).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.4445283033807374).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * -0.43843587057450184).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.23079678484166474).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.24296757608244463).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.6933510795197081).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.7747059716945244).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.6297402023667946).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.650250406527777).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.8327738427573091).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.8966188475674683).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.12025352080627527).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.029370019547682955).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)),
        cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)),
        cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)),
        cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)),
        cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)),
        cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
            cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
            cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
            cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
            cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.6542790087648793).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * -0.9830764940337477).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.7079366355498636).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.7127191144130105).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.5003181025167607).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.5392160412281468).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.4944938908636658).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.027211174863570817).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.5893795615335414).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.831516002652599).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.21350946680641048).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.42458233054252953).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.14729238052848453).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.19127454959401033).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.00982266418345571).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.018435329325373753).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.2092460914861244).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.08850669970348643).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.04816660891478307).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.05287080313477205).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.5144804279802232).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.2288739622948249).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.6539308607246773).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.9590761478286578).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.6105530873621177).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.5623428113606904).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.4541035216184288).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * -0.22652122700916058).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.09920368129230818).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.020249875179765953).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.7703835607337791).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.7508123024973197).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.9299380908209051).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.8609214882659385).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.6603148238966917).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.6664072567029273).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.011997302735339959).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.02416809397611926).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.7541471791694208).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.6727922869946045).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.21828350563706272).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.2387937097980442).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.8775865857149596).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.9414315905251189).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.5077173122630191).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.4168338110044266).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.493850693839934).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.46824735745938767).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.2984751103100736).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.7975917880942631).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.2590669520927105).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.46553678230138035).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.4922863320894708).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.4386037696673656).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.9729214362671511).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.9612016987900408).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.4556017204511883).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.4602146990123172).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.17115863024938213).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.07406694571515549).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.04747985536414887).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.0015617338005978266).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.2389354663504067).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.2865947391710613).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.5880773071541381).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.6362285069775276).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.3964494752371541).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.38670528408761545).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.011734933093958058).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.0011415796799869179).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.5924971027747271).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.6771826672314938).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.42942159755003484).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.5342946187446849).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * -0.8039587731906531).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.6712120667598861).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.878510082642783).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.8658791452001359).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.13314967964918875).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.3134985834412089).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.13421982786758235).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.14142059663243078).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.24729161215179005).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.1789596367298805).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.7475635765288697).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.8844707307377268).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.599747845729294).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.6253511821098403).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.9185238680705767).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.5823594541452338).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.017602831844571624).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.18886699836409832).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.4113331864284153).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.46501574885052055).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.7427018606296518).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.7309821231525422).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.4572604632711416).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.45264748471001387).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.8287439256872393).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.9260304983482223).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.5539049867836513).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.5048633976189045).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.17394491383358626).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.22160418665424148).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.24017847920109392).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.19202727937770428).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * -0.37039764324017677).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.38014183438971544).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.34101503555577156).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.35389154832971653).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.6559023537995501).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.5712167893427836).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.4498659567527707).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.34499293555812066).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.4151204811787974).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.5478671876095643).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.6044391967350843).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.5918082592924367).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.3382065832034761).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.5185554869954963).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.3976402333451519).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.3904394645803035).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.44626364529659257).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.8725148941782631).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.7580489709662166).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * 0.6211418167573595).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        (cirq.Y**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 0)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.7988745176237023).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * -0.43623002042232994).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.6854509025876576).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.6806684237245106).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.895797965119231).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.8569000264078449).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.5874420850315563).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.1201593690314567).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.1662456403979169).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.07589080072114174).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.7304236667431359).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.941496530479255).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.20225972132064465).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.15827755225511886).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.4344243610529689).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.46268235456179807).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.8068213968674496).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.509068605677839).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.48423867254446107).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.48894286676445003).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.15393657844081263).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.13166988724458512).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.9167642676321308).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.7780904452638893).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.9446189706702058).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.9928292466716331).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.5611001142888932).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * -0.3335178196796271).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.9320005175083301).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.8530467113957879).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.43500767720566996).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.41543641896921035).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.7467429096710533).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.5376024887578965).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.2245283033807833).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * -0.21843587057454775).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.5287967848416878).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.5409675760824668).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.6406489204802666).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.5592940283054504).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.2577402023668132).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.278250406527795).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.9067738427572684).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.9706188475674273).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.619746479193709).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.710629980452301).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)),
        cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)),
        cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)),
        cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)),
        cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)),
        cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
            cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
            cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
            cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
            cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.5842790087648996).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.9469235059662741).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.7059366355498733).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.7107191144130203).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.9796818974832071).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.9407839587718211).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.6095061091362723).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.9232111748636281).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.5926204384664704).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.35048399734741176).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.5284905331935638).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.3174176694574447).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.8852923805284783).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.929274549594004).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.9541773358165268).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.9824353293253562).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.9767539085138666).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.7254933002965229).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.9381666089148069).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.9428708031347959).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.8124804279802466).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.5268739622948487).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.8739308607246958).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.8209238521713237).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.8325530873621259).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.7843428113606987).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.7358964783815413).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * 0.9634787729908084).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.34679631870769856).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.42575012482024077).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.41561643926621195).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.43518769750267156).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.8480619091791521).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.6389214882659956).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.4403148238967388).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.4464072567029743).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.28600269726468336).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.27383190602390434).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.579852820830554).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.6612077130053702).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.590283505637045).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.6107937097980273).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.8035865857150007).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.8674315905251597).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.7522826877369967).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.8431661889955893).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.X**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(0, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 0)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.6438506938399094).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.618247357459362).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.07047511031002901).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.5695917880942174).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.4070669520927599).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.6135367823014299).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.5682863320894853).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.5146037696673801).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.28907856373285357).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.30079830120996326).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.6756017204512074).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.6802146990123358).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.6911586302494148).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.44593305428487634).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.39452014463587903).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.44356173380062575).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.4290645336496083).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.38140526082895393).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.5160773071541702).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.564228506977561).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.6204494752371521).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.6107052840876123).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.9502650669060344).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.9631415796799797).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.8895028972252971).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.8048173327685305).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.6805784024500074).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.5757053812553574).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * -0.8799587731906682).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.7472120667599012).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.5825100826428156).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.5698791452001684).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.9028503203508277).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.7225014165588084).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.3857801721324489).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.3785794033676002).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.10329161215178768).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.3229596367298828).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.3035635765288527).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.4404707307377103).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.7497478457292671).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.7753511821098146).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.8534761319293775).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.35435945414518916).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.16560283184462107).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.04086699836404887).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.4873331864284298).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.541015748850535).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.0047018606296570335).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.007017876847452668).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.6772604632711591).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.6726474847100307).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.6512560743127291).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.40603049834819016).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.9959049867836792).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.9468633976189325).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.8419449138336009).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.8896041866542553).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.16817847920112608).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.12002727937773534).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * -0.5943976432401735).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.6041418343897134).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.6209849644442211).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.6081084516702759).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.8260976462004742).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.9107832106572408).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.6601340432472717).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.7650070644419217).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.49112048117881246).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.6238671876095794).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.9004391967350515).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.8878082592924043).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.6257934167965067).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.4454445130044874).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.12235976665487905).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.12956053541972776).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.30226364529658795).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.7285148941782584).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.31404897096620005).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * 0.17714181675734245).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.5516614516047799).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.6174795220715865).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.4327711187160072).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.05062333421393557).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.3177840441511373).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.10047261856343086).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.5094803678807461).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.477422600327394).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.6408765210346724).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.6213948502194439).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.7032192054252008).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.754622217740198).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.9073671101422918).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.7688260728280146).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.8617637363416806).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.9336663643285862).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.3929732311767222).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.4097429307239244).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.0552051208550207).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.04849439530424264).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.9954710267271799).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.9922667609489023).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.08109954594056305).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.03439016849657811).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.11890354904913102).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.06799568729138893).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.6030454946335517).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.5869432193241655).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * -0.9975512288793414).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.9798328527655973).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.676440254578787).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.9238318053231387).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.7743905036170879).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.8501311900075205).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.6828230291151024).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.7440183043132079).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.06546313715369771).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.05739220357069274).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.03844537611129621).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.037517804558631546).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.782361625590525).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.9364903862480225).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.7611409474788069).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.8031117186780351).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.38150923394940456).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.37485924771904144).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.03297060514310833).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.3917017537983911).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
            cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
            cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
            cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
            cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)),
        cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)),
        cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)),
        cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)),
        cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.5641935842445645).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.4983755137777578).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.24179059583774581).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.7251850487676863).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.32084588367729194).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.5381573092649984).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.019062576518183987).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.01299519103516814).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.22619984017981742).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.2456815109950459).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.8617595478187416).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.9131625601337389).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.24317615795692585).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.38171719527120296).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.9034580610029361).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.9753606889898416).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.5871899251539519).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.603959624701154).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.29703548124351364).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.3037462067942906).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * -0.20718859840113155).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.2103928641794091).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.18030203332281788).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.2270114107668028).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.04128661851581855).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.1456126178247014).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.8499898074110996).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.8660920827204859).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.26992216901673105).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.24730625066166856).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.4845073865505883).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.8842353266486614).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.8911052487304801).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.8153645623400477).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.0158265769954911).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.07702185219359665).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.5014707755967253).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.5095417091797303).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * 0.3068636250628814).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.30779119661554605).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.5183942238917469).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.7995422120531994).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.9961315227572937).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.9618977060434781).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.26285448551587504).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.26950447174623815).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.6934649565591651).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * 0.947803894785552).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.X**0.5).on(cirq.GridQubit(0, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 0)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.08621640979886422).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.16334365608168644).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.3973572916277998).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.396326411747794).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.5427073576530422).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.5424147092534605).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.09003675765506945).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.34202849142196157).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.8983264693104055).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.7067732133063435).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.705156509293045).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.6244998637478164).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.15790347048791883).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.18947787438082972).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.8024559428448615).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.7589602352735803).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.8696926792305255).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.8516181998325968).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.8756084230940031).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.8808339440806644).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.24320434330005752).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.7125304945256264).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.9897343640361297).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.9074614067078688).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.9497630264840345).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.9177909707695425).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.12861597882367556).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.1299917767076041).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.13388452450572944).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.12593963181169407).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.9621689450218167).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.8955807139987333).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.7528365530460183).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.7258226701533779).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.7596124788130051).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.7153118414371823).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.6814566172688604).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.7119632677360634).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)),
        cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.08867615219877248).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.16088391368177818).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.5836051427906996).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.5846360226707056).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.6636695068149479).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.6633768584153672).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.7278338235086499).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.2957685744316189).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.7470909692987385).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.9386442253028005).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.534116953419378).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.6147735989646066).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.057788292865813835).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.08936269675872473).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.9720523226063322).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.9285566150350509).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.24050825583717475).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.22243377643924597).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.968723820269696).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.9634982992830347).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.5154066862373383).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.04608053501176949).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.24375561287182076).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.3465598421278222).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.6402034399153681).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.608231384200875).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.4706912009416499).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.4720669988255795).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.1947423470531135).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.2026872397471489).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.518418784954393).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.37616844397494287).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.13212668683985648).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.15914056973249802).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.698842568523934).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.7431432058997568).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.3162523839911777).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.28574573352397464).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 0)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.9936614516048078).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.9405204779283867).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.37922888128394683).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.862623334213893).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.792215955848905).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.9904726185633891).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.6765196321192446).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.7085773996725973).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.4948765210346792).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.4753948502194507).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.40721920542516743).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.45862221774016465).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.019367110142323812).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.11917392717195331).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.04776373634167188).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.11966636432857744).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.6929732311767329).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.7097429307239397).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.9847948791450413).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.9915056046958216).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.40547102672717017).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.40226676094889036).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.14290045405943544).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.1896098315034204).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.41690354904915433).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.23000431270863436).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.5270454946335372).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.510943219324151).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.48044877112063566).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.45783285276557767).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.08044025457880374).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.48016819467688143).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.9203905036170812).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.9961311900075136).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.12917697088491722).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.06798169568681166).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.5814631371537482).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.5733922035707443).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.6284453761113048).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.6275178045586413).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.7803616255905353).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.9384903862480122).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.5008590525212017).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.45888828132197124).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.5784907660505968).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.5851407522809633).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.10497060514307784).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.46370175379836065).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
            cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
            cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
            cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
            cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)),
        cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)),
        cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)),
        cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)),
        cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.9938064157554087).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.9403755137777857).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.5702094041622093).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.08681495123226317).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.789154116322751).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.571842690735044).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.7949374234818247).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.8269951910351775).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.08019984017982425).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.09968151099505272).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.8422404521812253).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.7908374398662281).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.6448238420430421).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.506282804728765).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.28254193899705515).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.21063931101014957).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.28718992515393654).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.30395962470114324).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.7429645187565517).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.7362537932057713).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.3828114015988804).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.3796071358206017).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.043697966677180636).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.0030114107668043153).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.25671338148420475).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.4436126178247247).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.7739898074110851).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.7900920827204714).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.7919221690167495).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.7693062506616914).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * -0.919492613449433).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.5197646733513552).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.9628947512695266).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.9613645623400409).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.8278265769955084).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.889021852193614).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.9825292244032231).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.9744582908202193).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * 0.8968636250628911).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.8977911966155546).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.5203942238917367).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.801542212053188).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.2581315227573).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.30010229395653043).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.6971455144841298).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.6904955282537633).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.6214649565591956).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.9801961052144784).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.X**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.5757835902011161).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.8253436560816667).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.5646427083721929).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.5656735882521988).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.10070735765308102).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.10041470925350265).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.1299632423448818).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.5620284914219106).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.15632646931043123).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.03522678669363078).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.6288434907069298).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.7095001362521582).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.732096529512105).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.7005221256191941).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.13445594284484547).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.09096023527356352).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.5716926792305023).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.5536181998325734).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.9516084230940176).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.9568339440806789).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.27279565669992845).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.1965304945256404).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.3937343640361464).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.4965385932921524).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.2382369735159425).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.2702090292304356).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.905384021176354).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.9040082232924209).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.7978845245057673).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.7899396318117285).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.964168945021872).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.893580713998678).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.435163446953961).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.46217732984660476).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.4283875211869742).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.4726881585628004).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.7965433827311167).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.7660367322639136).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)),
        cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.7506761521987528).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * -0.5011160863182021).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.37839485720929306).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.3773639773292872).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.8943304931850955).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.894623141584675).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.9478338235086012).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.5157685744315735).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.005090969298765407).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.19664422530282744).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.7998830465805966).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.7192264010353682).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.9477882928658377).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.9793626967587485).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.359947677393651).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.403443384964933).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.5385082558371981).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.5204337764392692).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.9552761797302897).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.9605017007169508).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.0005933137626453817).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.46991946498821424).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.8397556128717996).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.9425598421278055).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.17179656008465377).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.20376861579914693).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.495308799058324).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.49393300117439093).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.858742347053148).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.8666872397471868).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.5204187849544483).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.37816844397499816).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.9441266868398739).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.9711405697325176).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.4891574314760486).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.44485679410022244).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.8382523839912006).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.8077457335239976).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.5888745176237674).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * -0.22623002042239165).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.6794509025876863).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.6746684237245404).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.4557979651193263).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.41690002640794016).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.1005579149686249).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.56784063096872).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.6202456403978841).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.3781091992788255).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.956423666743059).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.8325034695208208).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.41625972132062794).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.3722775522551022).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.45757563894697817).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.4293176454381487).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.36482139686742276).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.0670686056778122).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.1857613274556098).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.1810571332356208).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.7400634215592568).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.9743301127553455).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.25676426763207516).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.5619095547360591).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.38938102932976887).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.3411707533283418).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.13110011428881016).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * 0.09648218032046488).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.2700005175083498).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.1910467113958076).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.006992322794356819).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.026563581030815846).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.5872570903291188).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.7963975112422756).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.43547169661907276).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.44156412942530826).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.5772032151582435).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.5650324239174633).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.6426489204801907).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.5612940283053744).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.8582597976331332).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * 0.8377495934721519).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.8712261572428549).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.8073811524326956).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.8397464791936613).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.930629980452254).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)),
        cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)),
        cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)),
        cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)),
        cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)),
        cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
            cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
            cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
            cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
            cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.37427900876496123).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.7369235059663369).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.6999366355499054).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.7047191144130511).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.5803181025168881).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.6192160412282741).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.07849389086390429).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.38878882513619073).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.13862043846650543).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.1035160026525532).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.754490533193488).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.5434176694573679).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.9007076194715385).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.8567254504060127).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.15382266418352536).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.12556467067469587).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.5347539085138397).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.8325066997034515).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.3918333910851223).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.3871291968651333).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.29351957201968526).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.579126037705083).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.46606913927525023).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.1609238521712663).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.5014469126378489).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.5496571886392757).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.3058964783814538).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * 0.5334787729907289).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.3152036812922806).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.2362498751797384).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.026383560733814825).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.006812302497355796).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.18206190917932413).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.027078511733832647).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.2196851761031195).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * -0.21359274329688396).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.8199973027352478).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.832168093976028).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.5818528208304781).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.6632077130052944).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.2937164943630092).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * 0.27320629020202797).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.5815865857151237).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.6454315905252832).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.5322826877370442).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.6231661889956362).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.X**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 0)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.9061493061601683).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.9317526425407147).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.6135248896901003).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.11440821190591195).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.8510669520929084).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.9424632176984219).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.7962863320895299).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.7426037696674247).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.07507856373287025).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.08679830120998447).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.6643982795487398).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.6597853009876091).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.25115863024950946).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.005933054284972138).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.2794798553640372).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.230438266199295).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.4330645336496544).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.38540526082900006).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.30007730715426284).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.34822850697765584).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * -0.7075505247628513).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.7172947159123899).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.16373493309398734).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.15085842032004207).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.6644971027746309).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.7491826672313975).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.010578402450135117).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.09429461874451604).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.8920412268092872).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.9752120667599447).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.30548991735708686).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.318120854799734).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.010850320350880316).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.169498583441139).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.054219827867455876).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.06142059663230459).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.32870838784822615).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.7549596367298966).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.9715635765288021).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * 0.8915292692623403).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.8002521542708073).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.774648817890261).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.16947613192924818).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.3296405458549402).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.6096028318447693).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.40313300163609944).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.7153331864284722).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.7690157488505774).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.209298139370324).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.22101787684743823).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.6627395367287836).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.6673525152899142).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.9087439256873666).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.8460304983480961).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.32190498678375845).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.2728633976190163).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.8459449138336471).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.8936041866543014).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.04782152079877905).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.09597272062217206).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.7336023567598287).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.7238581656102899).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.49301503555580056).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.5058915483297458).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.7279023537994534).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.6432167893426869).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.009865956752601861).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.0950070644420493).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.7191204811788571).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.851867187609624).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.21156080326504628).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.22419174070769343).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.48220658320354487).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.6625554869955641).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.3176402333450257).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.310439464580177).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.1297363547034259).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.2965148941782446).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.9820489709661495).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * 0.8451418167572918).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.5188745176237864).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * -0.15623002042241071).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.6774509025876966).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.6726684237245518).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.9757979651193572).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.9369000264079712).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.9965579149686958).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.5361593690312092).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.5617543596021294).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.8038908007211836).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.30157633325696676).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.09050346952084656).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.8457402786793784).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.8897224477448996).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.5784243610530388).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.6066823545618683).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.44917860313258545).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.746931394322196).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.9242386725443664).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.9289428667643553).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.9619365784407211).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.6763301127553222).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.03676426763205716).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.34190955473604107).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.16738102932976004).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.11917075332833355).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.6788998857112175).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * 0.9064821803204925).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.716000517508356).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.6370467113958149).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.820992322794365).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.8405635810308246).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.36525709032917614).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.5743975112423332).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.6554716966190274).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.6615641294252584).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.2792032151582201).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.26703242391743887).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.023351079519834027).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.10470597169464968).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.7697402023668831).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.7902504065278677).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.7972261572428959).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.7333811524327367).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.4202535208063547).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.32937001954776157).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)),
        cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)),
        cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)),
        cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)),
        cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)),
        cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
            cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
            cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
            cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
            cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.30427900876498026).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.666923505966356).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.6979366355499168).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.7027191144130615).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.8996818974830809).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.8607839587716949).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.9744938908639662).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.5072111748638711).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.6793795615334856).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.9215160026525442).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.5035094668065377).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.714582330542658).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.16270761947154028).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.11872545040601902).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.8101773358164577).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.8384353293252871).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.2792460914861695).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.01850669970344215).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.49816660891490155).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.5028708031348905).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.004480427980338054).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.28112603770506084).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.24606913927523225).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.05907614782875167).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.2794469126378407).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.3276571886392672).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.5041035216185739).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * -0.2765212270092988).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.1307963187077267).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.20975012482027006).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.8403835607338236).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.8208123024973651).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.039938090820618236).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.24907851173377474).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.4396851761030696).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * -0.4335927432968386).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.5219973027352212).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.5341680939760024).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.08414717916954664).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.0027922869947304236).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.07828350563697334).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.0987937097979534).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.5075865857151647).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.5714315905253242).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.20771731226294082).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.11683381100434823).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.Y**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 0)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.7561493061601958).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.781752642540741).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.8415248896901449).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.3424082119059566).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.9990669520929577).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.7944632176983725).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.8722863320895433).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.8186037696674426).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.6629214362671234).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.6512016987900138).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.4443982795487218).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.4397853009875912).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.7711586302495393).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.5259330542850031).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.16252014463598846).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.21156173380073065).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.8989354663503306).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.9465947391709849).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.22807730715429672).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.2762285069776852).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * -0.48355052476285504).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.4932947159123926).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.7982650669060048).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.8111415796799502).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.8175028972253934).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.7328173327686268).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.8794215975498231).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.9842946187444742).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.8160412268092694).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.9487879332400408).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.6014899173570537).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.6141208547997015).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.9531496796491027).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.866501416558878).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.4657801721325751).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.4585794033677264).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.4727083878482263).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.8989596367298968).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.527563576528785).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.6644707307376426).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.6502521542708336).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.6246488178902884).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.05852386807079644).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.5576405458549848).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.7576028318448186).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.5511330016361488).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.79133318642849).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.8450157488505907).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.9472981393703223).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.9590178768474319).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.44273953672876565).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.4473525152898963).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.5712560743126024).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.32603049834806397).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.763904986783784).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.7148633976190419).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.4860550861663379).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.43839581334568356).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.11982152079874969).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.1679727206221382).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.5096023567598313).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.4998581656102937).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.46898496444419163).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.4561084516702464).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.7540976462005708).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.8387832106573374).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.8998659567525601).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.794992935557909).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.7951204811788705).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.9278671876096419).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.08443919673492117).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.07180825929227404).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.48179341679643817).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.3014445130044189).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.20235976665500524).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.20956053541985398).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.273736354703426).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.15251489417824454).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.5380489709661325).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * 0.4011418167572748).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        (cirq.X**0.5).on(cirq.GridQubit(0, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 0)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.3196614516048859).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.38547952207169484).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.8152288812838089).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.7013766657862495).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.12221595584903099).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.33952738143673855).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.23451963211921778).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.2665773996725705).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.056876521034694004).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.03739485021947005).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.48078079457493167).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.4293777822599345).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.6446328898575795).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.7831739271718566).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.39423626365835546).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.3223336356714499).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.40702676882322575).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.390257069276019).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.10479487914523171).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.11150560469601203).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.6354710267271366).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.6322667609488568).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.8149004540594265).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.861609831503416).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.6890964509507758).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.8759956872912957).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.2990454946334938).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.2829432193241075).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.9144487711205713).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.8918328527655134).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.2924402545788629).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.6921681946769406).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.6416094963829359).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.5658688099925057).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.5651769708849738).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.5039816956868637).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.1294631371539041).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.12139220357089683).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.3984453761113394).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.39751780455867475).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.7743616255905674).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.9444903862479824).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.28685905252121613).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.24488828132199017).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.5415092339493901).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.5348592477190326).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.3209706051429841).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.6797017537982691).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
            cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
            cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
            cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
            cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)),
        cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)),
        cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)),
        cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)),
        cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.33219358424467277).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.2663755137778638).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.9937905958379286).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.5228149512321297).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.1191541163228786).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.09815730926482896).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.7630625765181485).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.7310048089647958).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.35780015982015645).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.3383184890049325).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.04575954781887384).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.09716256013387105).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.6911761579570534).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.8297171952713306).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.15945806100297222).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.23136068898987777).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.6128100748461002).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.5960403752988935).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.13703548124325787).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.14374620679403818).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.15281140159891393).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.1496071358206341).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.7156979666771761).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.6689885892331867).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.8492866185157253).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.6623873821752053).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.5459898074110394).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.5620920827204257).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.3579221690168138).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.3353062506617558).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.8685073865505079).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.7317646733514145).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.5248947512695437).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.600635437659974).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.7361734230044396).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.6749781478063295).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.5654707755969294).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.5735417091799366).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * 0.6668636250629246).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.6677911966155893).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.5263942238917069).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.8075422120531571).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.04413152275731896).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.08610229395654488).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.42285448551587074).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.4295044717462282).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.4054649565592893).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.7641961052145744).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.Y**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.5617835902010525).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.8113436560816032).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.5493572916278294).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.5483264117478236).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.7747073576531985).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.7744147092536157).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.7899632423447435).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.7779715085782299).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.06967353068949138).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.26122678669355454).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.6308434907068533).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.7115001362520819).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.5979034704878248).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.6294778743807357).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.13045594284479936).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.0869602352735174).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.3223073207695666).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.3403818001674931).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.8203915769059411).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.8151660559192776).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.17920434330011353).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.6485304945256825).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.6057343640362102).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.7085385932922116).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.19776302648411406).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.16579097076962546).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.007384021176433596).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.00600822329250055).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.7898845245058673).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.781939631811833).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.9701689450220378).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.8875807139985098).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.0008365530460956168).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.02617732984654818).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.007612478813077853).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.036688158562739326).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.7694566172689431).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.7999632677361507).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)),
        cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.7366761521986892).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * -0.4871160863181386).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.7356051427907281).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.7366360226707339).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.4316695068147915).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.4313768584152086).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.3921661764915394).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.8242314255685659).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.22090903070115833).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.029355774697097447).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.8018830465805213).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.7212264010352928).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.3822117071340921).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.3506373032411812).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.3559476773936038).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.39944338496488685).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.5674917441627332).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.5855662235606597).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.7272761797302438).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.7325017007169073).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.4514066862373966).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.017919464988172252).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.6277556128717449).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.7305598421277463).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.6077965600847104).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.639768615799199).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.6066912009417557).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.6080669988256887).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.850742347053257).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.8586872397472913).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.5264187849546164).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.38416844397516403).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.6198733131600651).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.5928594302674213).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.053157431475987546).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.008856794100170371).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.40425238399126495).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.3737457335240574).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.X**0.5).on(cirq.GridQubit(0, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 0)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.761661451604916).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.827479522071725).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.37277111871624163).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.11062333421370002).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.7677840441509273).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.5504726185632197).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.5794803678807904).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.5474226003274377).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.0891234789653003).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.10860514978052427).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.7767807945749653).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.7253777822599681).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.46736711014245313).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.328826072828176).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.7917637363416363).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.8636663643285419).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.107026768823215).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.09025706927600828).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.8552051208547063).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.848494395303926).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.04547102672712247).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.04226676094884716).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.9610995459405717).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.9143901684965867).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.3910964509507547).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.5779956872912702).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.2230454946334759).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.20694321932409412).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.3924487711205484).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.36983285276549044).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * -0.30355974542111586).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.09616819467696185).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.4956094963829416).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.4198688099925114).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.6228230291150043).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.6840183043131144).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.6454631371539489).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.6373922035709507).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.9884453761113445).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.9875178045586844).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.7723616255905777).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.9464903862479721).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.4511409474787776).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.4931117186780035).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * 0.4184907660506158).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * -0.42514075228097326).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.39297060514295473).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.7517017537982353).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
            cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
            cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
            cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
            cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)),
        cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)),
        cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)),
        cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)),
        cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.774193584244703).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.708375513777894).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.1817905958379791).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.6651850487679207).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.7708458836770796).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.9881573092647872).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.05093742348185972).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.08299519103521241).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.5038001598201507).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.4843184890049268).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.34175954781890744).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.39316256013390466).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.1968238420429139).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.05828280472863678).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.9734580610029804).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.954639311010114).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.912810074846111).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.8960403752989042).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.9029645187568041).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.8962537932060238).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.7428114015989191).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.7396071358206437).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.9396979666771735).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.8929885892331886).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.5512866185156997).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.36438738217518435).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.469989807411026).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.48609208272040777).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.8799221690168367).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.8573062506617788).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * -0.5354926134495134).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.13576467335143572).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.3788947512695494).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.4546354376599796).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.07582657699558236).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.13702185219369245).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * -0.9185292244030168).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.9104582908200186).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * -0.7431363749370657).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.7422088033844056).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.5283942238916967).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.8095422120531468).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.6938684772426748).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.6518977060434488).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.5371455144841352).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.5304955282537777).on(cirq.GridQubit(8, 5)),
        cirq.Rz(np.pi * 0.33346495655932323).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.6921961052146037).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.Y**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.7762164097989717).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * -0.5266563439184256).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.41264270837216277).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.41367358825216866).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.3327073576532407).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.33241470925365335).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.9900367576553064).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.5579715085782754).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * -0.8116735306894645).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.9967732133064724).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.035156509293171996).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.04550013625205651).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.29209652951219905).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.26052212561928817).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.5375440571552134).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.5810397647264999).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.6203073207695876).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.6383818001675187).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * -0.7443915769059233).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.7391660559192642).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.33679565669986794).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.13253049452570093).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.009734364036231385).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.11253859329223283).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.9902369735158686).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.9777909707696428).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.9586159788235369).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.9599917767074699).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.5461154754940948).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.5540603681881291).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.9721689450220954).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.8855807139984568).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.812836553046113).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.7858226701534692).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.8196124788130952).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.775311841437278).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.7085433827310339).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.6780367322638263).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)),
        cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.6013238478013305).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.8508839136818767).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.22639485720926408).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.22536397732925822).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.8736695068147584).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.873376858415171).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.17216617649158472).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.6042314255686158).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.9629090307011337).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.7713557746970705).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.13588304658049602).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * -0.05522640103526752).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.5077882928659317).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.5393626967588426).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.31205232260641236).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.26855661503512585).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.2694917441627076).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.2875662235606386).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.6512761797302304).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.6565017007168895).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.06459331376258938).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.5339194649881582).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.7762443871282764).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.673440157872275).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.5802034399152723).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.5482313842007837).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.35930879905821483).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.3579330011742818).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.4852576529467051).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.47731276025267083).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.5284187849546694).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.38616844397522154).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.19212668683995227).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.21914056973259607).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.7588425685240298).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.803143205899847).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.926252383991288).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.8957457335240803).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(0, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 0)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.30887451762385265).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.05376997957752308).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * 0.6714509025877274).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * -0.6666684237245782).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.5357979651194491).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * -0.4969000264080675).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * -0.3154420850311276).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.1518406309689674).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * 0.10775435960216559).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.3498908007212197).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * 0.07557633325704298).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.13549653047907945).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.6317402786793928).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.6757224477449232).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.31357563894691026).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.28531764543807964).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.8911786031326122).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.8110686056777761).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * -0.254238672544295).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * 0.25894286676428735).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.06793657844065232).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.21766988724474998).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * -0.6232357323680013).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.3180904452640219).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.4986189706702653).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.5468292466716921).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.8911001142886905).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * -0.6635178196794336).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.054000517508380204).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.024953288604164278).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.7370076772056071).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.717436418969148).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.3007429096706518).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.09160248875749502).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.6845283033811131).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * -0.6784358705748776).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.614796784841851).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.6269675760826288).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * -0.021351079519910485).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.10270597169472784).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.346259797633061).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * 0.3257495934720798).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.575226157243019).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.5113811524328596).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.2002535208064012).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.10937001954780803).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
            cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)),
        cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
            cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)),
        cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
            cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)),
        cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
            cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)),
        cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
            cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)),
        cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
            cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)),
        cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
            cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)),
        cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
            cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)),
        cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
            cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)),
        cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
            cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)),
        cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
            cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)),
        cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
            cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)),
        cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
            cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)),
        cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
            cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)),
        cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
            cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)),
        cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
            cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)),
        cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
            cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)),
        cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
            cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)),
        cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
            cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)),
        cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
            cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)),
        cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
            cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)),
        cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
            cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)),
        cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
            cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.09427900876504648).on(cirq.GridQubit(0, 5)),
        cirq.Rz(np.pi * 0.45692350596642217).on(cirq.GridQubit(0, 6)),
        cirq.Rz(np.pi * -0.6919366355499432).on(cirq.GridQubit(1, 4)),
        cirq.Rz(np.pi * 0.6967191144130923).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.6603181025170132).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.6992160412283948).on(cirq.GridQubit(1, 7)),
        cirq.Rz(np.pi * 0.3375061091358572).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.8047888251359522).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.8666204384665461).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.6244839973474919).on(cirq.GridQubit(2, 8)),
        cirq.Rz(np.pi * -0.277509466806614).on(cirq.GridQubit(3, 2)),
        cirq.Rz(np.pi * 0.4885823305427364).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.051292380528436224).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * 0.09527454959396654).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.29782266418359443).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.2695646706747638).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.7212460914861952).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.4234933002965835).on(cirq.GridQubit(3, 9)),
        cirq.Rz(np.pi * 0.8318333910850282).on(cirq.GridQubit(4, 1)),
        cirq.Rz(np.pi * -0.8271291968650358).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * -0.8984804279804103).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * 0.612873962295008).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.4139308607248262).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.7190761478288056).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.3865530873621846).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * 0.3383428113607581).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.9341035216186568).on(cirq.GridQubit(5, 0)),
        cirq.Rz(np.pi * -0.7065212270093999).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.5312036812922547).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.45224987517971027).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.7176164392661503).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.7371876975026093).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.7059380908204465).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.9150785117336027).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.900314823897071).on(cirq.GridQubit(6, 1)),
        cirq.Rz(np.pi * 0.9064072567033065).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.37200269726484647).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * 0.3598319060240686).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.0821471791696231).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.0007922869948057504).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * -0.8057164943630791).on(cirq.GridQubit(7, 2)),
        cirq.Rz(np.pi * 0.7852062902020979).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * 0.28558658571528767).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.3494315905254475).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.4277173122628932).on(cirq.GridQubit(8, 3)),
        cirq.Rz(np.pi * -0.33683381100430004).on(cirq.GridQubit(8, 4)),
    ]),
    cirq.Moment(operations=[
        (cirq.Y**0.5).on(cirq.GridQubit(0, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(0, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(1, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(2, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(4, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 9)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 0)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 8)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(6, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(8, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(9, 4)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * -0.30614930616027464).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * 0.3317526425408198).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.47447511030972117).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * -0.9735917880939186).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * 0.5569330479068944).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.3504632176982243).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * -0.8997136679104121).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * 0.9533962303325128).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.876921436267109).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.8652016987899993).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * 0.21560172045134118).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * -0.2202146990124718).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * -0.33115863024963454).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.0859330542850972).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.5114798553639346).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.46243826619919237).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * 0.8949354663502844).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * -0.9425947391709388).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.012077307154384783).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.0602285069777778).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * 0.18844947523714164).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * -0.17870528408759956).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * 0.31573493309401746).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * -0.3028584203200711).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * -0.7364971027745343).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * 0.8211826672313014).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * 0.4505784024503011).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * -0.3457053812556511).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * 0.5880412268092248).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * -0.7207879332399962).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.5105100826430439).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.49787914520039617).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * 0.15485032035094826).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.02549858344107104).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.025780172132672592).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.018579403367823877).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * 0.9047083878482265).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.6690403632700984).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * -0.8044364234712655).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * 0.6675292692624085).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
            cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)),
        cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
            cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)),
        cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
            cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)),
        cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
            cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)),
        cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
            cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)),
        cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
            cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)),
        cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
            cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)),
        cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
            cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)),
        cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
            cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)),
        cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
            cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)),
        cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
            cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)),
        cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
            cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)),
        cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
            cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)),
        cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
            cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)),
        cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
            cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)),
        cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
            cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)),
        cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
            cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)),
        cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
            cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)),
        cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
            cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)),
        cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
            cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        cirq.Rz(np.pi * 0.20025215427091245).on(cirq.GridQubit(1, 5)),
        cirq.Rz(np.pi * -0.17464881789036724).on(cirq.GridQubit(1, 6)),
        cirq.Rz(np.pi * 0.7425238680709213).on(cirq.GridQubit(2, 4)),
        cirq.Rz(np.pi * 0.7583594541448813).on(cirq.GridQubit(2, 5)),
        cirq.Rz(np.pi * -0.7983971681550331).on(cirq.GridQubit(2, 6)),
        cirq.Rz(np.pi * -0.995133001636297).on(cirq.GridQubit(2, 7)),
        cirq.Rz(np.pi * 0.9806668135714653).on(cirq.GridQubit(3, 3)),
        cirq.Rz(np.pi * -0.9269842511493647).on(cirq.GridQubit(3, 4)),
        cirq.Rz(np.pi * -0.8387018606296968).on(cirq.GridQubit(3, 5)),
        cirq.Rz(np.pi * 0.826982123152587).on(cirq.GridQubit(3, 6)),
        cirq.Rz(np.pi * -0.21726046327129284).on(cirq.GridQubit(3, 7)),
        cirq.Rz(np.pi * 0.2126474847101622).on(cirq.GridQubit(3, 8)),
        cirq.Rz(np.pi * 0.9887439256874939).on(cirq.GridQubit(4, 2)),
        cirq.Rz(np.pi * 0.7660304983479688).on(cirq.GridQubit(4, 3)),
        cirq.Rz(np.pi * -0.0899049867838656).on(cirq.GridQubit(4, 4)),
        cirq.Rz(np.pi * 0.04086339761912342).on(cirq.GridQubit(4, 5)),
        cirq.Rz(np.pi * -0.4820550861662918).on(cirq.GridQubit(4, 6)),
        cirq.Rz(np.pi * 0.4343958133456374).on(cirq.GridQubit(4, 7)),
        cirq.Rz(np.pi * -0.3358215207986571).on(cirq.GridQubit(4, 8)),
        cirq.Rz(np.pi * 0.3839727206220501).on(cirq.GridQubit(4, 9)),
        cirq.Rz(np.pi * -0.16239764324016084).on(cirq.GridQubit(5, 1)),
        cirq.Rz(np.pi * 0.17214183438970293).on(cirq.GridQubit(5, 2)),
        cirq.Rz(np.pi * -0.6450150355558295).on(cirq.GridQubit(5, 3)),
        cirq.Rz(np.pi * 0.6578915483297759).on(cirq.GridQubit(5, 4)),
        cirq.Rz(np.pi * 0.7999023537993563).on(cirq.GridQubit(5, 5)),
        cirq.Rz(np.pi * -0.7152167893425903).on(cirq.GridQubit(5, 6)),
        cirq.Rz(np.pi * -0.43013404324756527).on(cirq.GridQubit(5, 7)),
        cirq.Rz(np.pi * 0.5350070644422154).on(cirq.GridQubit(5, 8)),
        cirq.Rz(np.pi * -0.9768795188210849).on(cirq.GridQubit(6, 2)),
        cirq.Rz(np.pi * 0.8441328123903135).on(cirq.GridQubit(6, 3)),
        cirq.Rz(np.pi * -0.9724391967348236).on(cirq.GridQubit(6, 4)),
        cirq.Rz(np.pi * 0.9598082592921758).on(cirq.GridQubit(6, 5)),
        cirq.Rz(np.pi * -0.6262065832036139).on(cirq.GridQubit(6, 6)),
        cirq.Rz(np.pi * 0.8065554869956344).on(cirq.GridQubit(6, 7)),
        cirq.Rz(np.pi * 0.23764023334489953).on(cirq.GridQubit(7, 3)),
        cirq.Rz(np.pi * -0.23043946458005082).on(cirq.GridQubit(7, 4)),
        cirq.Rz(np.pi * -0.7057363547034308).on(cirq.GridQubit(7, 5)),
        cirq.Rz(np.pi * 0.27948510582175573).on(cirq.GridQubit(7, 6)),
        cirq.Rz(np.pi * 0.7939510290339188).on(cirq.GridQubit(8, 4)),
        cirq.Rz(np.pi * -0.9308581832427758).on(cirq.GridQubit(8, 5)),
    ]),
    cirq.Moment(operations=[
        (cirq.X**0.5).on(cirq.GridQubit(0, 5)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(0, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(1, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(1, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(2, 7)),
        (cirq.X**0.5).on(cirq.GridQubit(2, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 2)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(3, 6)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(3, 7)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(3, 9)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 1)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 3)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 4)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(4, 8)),
        (cirq.Y**0.5).on(cirq.GridQubit(4, 9)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 0)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 1)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 2)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(5, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 6)),
        (cirq.X**0.5).on(cirq.GridQubit(5, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(5, 8)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 1)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(6, 4)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(6, 7)),
        cirq.PhasedXPowGate(phase_exponent=0.25,
                            exponent=0.5).on(cirq.GridQubit(7, 2)),
        (cirq.Y**0.5).on(cirq.GridQubit(7, 3)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 5)),
        (cirq.X**0.5).on(cirq.GridQubit(7, 6)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 3)),
        (cirq.Y**0.5).on(cirq.GridQubit(8, 4)),
        (cirq.X**0.5).on(cirq.GridQubit(8, 5)),
        (cirq.Y**0.5).on(cirq.GridQubit(9, 4)),
    ]),
])

" data-is-ci-config-file="false" id="js-blob-toggle-graph-preview"></div>
<div class="blob-viewer" data-path="BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py" data-type="simple" data-url="/panfeng/sycamore20/-/blob/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py?format=json&amp;viewer=simple">
<div class="text-center gl-mt-4 gl-mb-3">
<span class="gl-spinner gl-spinner-orange gl-spinner-md qa-spinner" aria-label="Loading"></span>
</div>

</div>


</article>
</div>

<div class="modal" id="modal-remove-blob">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Delete circuit_n53_m20_s0_e0_pABCDCDAB.py</h3>
<button aria-label="Close" class="close" data-dismiss="modal" type="button">
<span aria-hidden>&times;</span>
</button>
</div>
<div class="modal-body">
<form class="js-delete-blob-form js-quick-submit js-requires-input" action="/panfeng/sycamore20/-/blob/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="delete" /><input type="hidden" name="authenticity_token" value="8CViQfqEauqWOBhZMvv5l2nl57PwgF2xaGAKJFc0pcW9TypmTxG/XfrNKOhBsY/2Q7u+a3yu+fsZOWA6bqoulg==" /><div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-06d65811d828f8a6a8238c4129491f8e">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-06d65811d828f8a6a8238c4129491f8e" class="form-control js-commit-message" placeholder="Delete circuit_n53_m20_s0_e0_pABCDCDAB.py" required="required" rows="3">
Delete circuit_n53_m20_s0_e0_pABCDCDAB.py</textarea>
</div>
</div>
</div>

<div class="form-group row branch">
<label class="col-form-label col-sm-2" for="branch_name">Target Branch</label>
<div class="col-sm-10">
<input type="text" name="branch_name" id="branch_name" value="refine" required="required" class="form-control js-branch-name ref-name" />
<div class="js-create-merge-request-container">
<div class="form-check gl-mt-3">
<input type="checkbox" name="create_merge_request" id="create_merge_request-e06bcc5af389dafdf1b840e0204193d2" value="1" class="js-create-merge-request form-check-input" checked="checked" />
<label class="form-check-label" for="create_merge_request-e06bcc5af389dafdf1b840e0204193d2">Start a <strong>new merge request</strong> with these changes
</label></div>

</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="refine" class="js-original-branch" />

<div class="form-group row">
<div class="offset-sm-2 col-sm-10">
<button name="button" type="submit" class="btn gl-button btn-danger btn-remove-file">Delete file</button>
<a class="btn gl-button btn-cancel" data-dismiss="modal" href="#">Cancel</a>
</div>
</div>
</form></div>
</div>
</div>
</div>

<div class="modal" id="modal-upload-blob">
<div class="modal-dialog modal-lg">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Replace circuit_n53_m20_s0_e0_pABCDCDAB.py</h3>
<button aria-label="Close" class="close" data-dismiss="modal" type="button">
<span aria-hidden>&times;</span>
</button>
</div>
<div class="modal-body">
<form class="js-quick-submit js-upload-blob-form" data-method="put" action="/panfeng/sycamore20/-/update/refine/BipartitionBatch/loadtensor/Sycamore/circuit_n53_m20_s0_e0_pABCDCDAB.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="yBjHsREV5ML1lDDhJ4qLfzrYUa1opVsEoBRLymlLwnGFco+WpIAxdZlhAFBUwP0eEIYIdeSL/07RTSHUUNVJIg==" /><div class="dropzone">
<div class="dropzone-previews blob-upload-dropzone-previews">
<p class="dz-message light">
Attach a file by drag &amp; drop or <a class="markdown-selector" href="#">click to upload</a>
</p>
</div>
</div>
<br>
<div class="dropzone-alerts gl-alert gl-alert-danger gl-mb-5 data" style="display:none"></div>
<div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-2b20baa43f40faab6fc4d8396fbda401">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-2b20baa43f40faab6fc4d8396fbda401" class="form-control js-commit-message" placeholder="Replace circuit_n53_m20_s0_e0_pABCDCDAB.py" required="required" rows="3">
Replace circuit_n53_m20_s0_e0_pABCDCDAB.py</textarea>
</div>
</div>
</div>

<div class="form-group row branch">
<label class="col-form-label col-sm-2" for="branch_name">Target Branch</label>
<div class="col-sm-10">
<input type="text" name="branch_name" id="branch_name" value="refine" required="required" class="form-control js-branch-name ref-name" />
<div class="js-create-merge-request-container">
<div class="form-check gl-mt-3">
<input type="checkbox" name="create_merge_request" id="create_merge_request-9a5fefd9d0e792541ff0a0be225afe1d" value="1" class="js-create-merge-request form-check-input" checked="checked" />
<label class="form-check-label" for="create_merge_request-9a5fefd9d0e792541ff0a0be225afe1d">Start a <strong>new merge request</strong> with these changes
</label></div>

</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="refine" class="js-original-branch" />

<div class="form-actions">
<button name="button" type="button" class="btn gl-button btn-success btn-upload-file" id="submit-all"><i aria-hidden="true" data-hidden="true" class="fa fa-spin fa-spinner js-loading-icon hidden"></i>
Replace file
</button><a class="btn gl-button btn-cancel" data-dismiss="modal" href="#">Cancel</a>

</div>
</form></div>
</div>
</div>
</div>

</div>


</div>
</div>
</div>
</div>

<div class="footer-message" style="background-color: #307df8;color: #ffffff"><p>Provided by Institute of Theoretical Physics, Chinese Academy of Sciences. Please contact  <a href="mailto:support@itp.ac.cn">support@itp.ac.cn</a> for more information.</p></div>
<script>
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded', 'qa-js-lazy-loaded');
  });
}

//]]>
</script>

</body>
</html>

