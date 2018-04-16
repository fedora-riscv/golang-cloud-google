# Circular dependency with golang.org/x/oauth2 and golang.org/x/build
%bcond_without bootstrap
# Run tests in check section
%bcond_with check

%global goipath         cloud.google.com/go
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
%global oldgoipath      google.golang.org/cloud
%global oldgoname       %gorpmname %{oldgoipath}
Version:                0.20.0

%global common_description %{expand:
Google Cloud Client Libraries for Go.}

%gometa

Name:    %{goname}
Release: 1%{?dist}
Summary: Google Cloud Client Libraries for Go
License: ASL 2.0
URL:     %{gourl}
Source:  %{gosource}
Source1: google-cloud-go-0.20.0-vendor.tar.gz

%if %{without bootstrap}
BuildRequires: golang(github.com/golang/mock/gomock)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/ptypes)
BuildRequires: golang(github.com/golang/protobuf/ptypes/any)
BuildRequires: golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires: golang(github.com/google/btree)
BuildRequires: golang(github.com/google/go-cmp/cmp)
BuildRequires: golang(github.com/google/pprof/profile)
BuildRequires: golang(github.com/googleapis/gax-go)
BuildRequires: golang(golang.org/x/build/kubernetes)
BuildRequires: golang(golang.org/x/build/kubernetes/api)
BuildRequires: golang(golang.org/x/build/kubernetes/gke)
BuildRequires: golang(golang.org/x/debug)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/oauth2/jwt)
BuildRequires: golang(golang.org/x/sync/errgroup)
BuildRequires: golang(golang.org/x/sync/semaphore)
BuildRequires: golang(golang.org/x/text/language)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(google.golang.org/api/bigquery/v2)
BuildRequires: golang(google.golang.org/api/cloudbuild/v1)
BuildRequires: golang(google.golang.org/api/clouddebugger/v2)
BuildRequires: golang(google.golang.org/api/cloudresourcemanager/v1)
BuildRequires: golang(google.golang.org/api/cloudtrace/v1)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(google.golang.org/api/container/v1)
BuildRequires: golang(google.golang.org/api/gensupport)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/iterator)
BuildRequires: golang(google.golang.org/api/option)
BuildRequires: golang(google.golang.org/api/storage/v1)
BuildRequires: golang(google.golang.org/api/support/bundler)
BuildRequires: golang(google.golang.org/api/transport)
BuildRequires: golang(google.golang.org/api/transport/grpc)
BuildRequires: golang(google.golang.org/api/transport/http)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/label)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/metric)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/monitoredres)
BuildRequires: golang(google.golang.org/genproto/googleapis/appengine/logging/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/bigtable/admin/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/bigtable/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/audit)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/bigquery/datatransfer/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/dataproc/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/language/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/language/v1beta2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/oslogin/common)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/oslogin/v1beta)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/speech/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/speech/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/videointelligence/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/videointelligence/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/videointelligence/v1beta2)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/vision/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/cloud/vision/v1p1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/container/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/datastore/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/clouddebugger/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/cloudprofiler/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/cloudtrace/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/devtools/cloudtrace/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/firestore/v1beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/iam/admin/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/iam/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/logging/type)
BuildRequires: golang(google.golang.org/genproto/googleapis/logging/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/longrunning)
BuildRequires: golang(google.golang.org/genproto/googleapis/monitoring/v3)
BuildRequires: golang(google.golang.org/genproto/googleapis/privacy/dlp/v2)
BuildRequires: golang(google.golang.org/genproto/googleapis/privacy/dlp/v2beta1)
BuildRequires: golang(google.golang.org/genproto/googleapis/privacy/dlp/v2beta2)
BuildRequires: golang(google.golang.org/genproto/googleapis/pubsub/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/rpc/code)
BuildRequires: golang(google.golang.org/genproto/googleapis/rpc/errdetails)
BuildRequires: golang(google.golang.org/genproto/googleapis/rpc/status)
BuildRequires: golang(google.golang.org/genproto/googleapis/spanner/admin/database/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/spanner/admin/instance/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/spanner/v1)
BuildRequires: golang(google.golang.org/genproto/googleapis/type/latlng)
BuildRequires: golang(google.golang.org/genproto/protobuf/field_mask)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/keepalive)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/status)
%endif

%if %{with check}
BuildRequires: golang(github.com/google/go-cmp/cmp)
BuildRequires: golang(google.golang.org/api/iterator)
BuildRequires: golang(google.golang.org/api/option)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%package -n compat-%{oldgoname}-devel
Summary:    %{summary}
BuildArch:  noarch

%description -n compat-%{oldgoname}-devel
%{common_description}

This package contains compatibility glue for code that still imports the
%{oldgoipath} Go namespace.


%prep
%forgeautosetup
%if %{with bootstrap}
%autosetup %{?forgesetupargs} -N -T -D -a 1
%endif


%install
%goinstall

install -m 0755 -vd %{buildroot}%{gopath}/src/%(dirname %{oldgoipath})
ln -s %{gopath}/src/%{goipath} %{buildroot}%{gopath}/src/%{oldgoipath}


%if %{with check}
%check
%gochecks -d storage
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTORS AUTHORS old-news.md


%files -n compat-%{oldgoname}-devel
%dir %{gopath}/src/%(dirname %{oldgoipath})
%{gopath}/src/%{oldgoipath}


%changelog
* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.20.0-1
- First package for Fedora

