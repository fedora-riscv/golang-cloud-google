# Generated by go2rpm 1.6.0
%bcond_without check
%bcond_with bootstrap
%global debug_package %{nil}

# https://github.com/GoogleCloudPlatform/google-cloud-go
%global goipath         cloud.google.com/go
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
Version:                0.103.0
%global tag             bigtable/v1.16.0
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Go packages for Google Cloud Platform services.}

%global golicenses      LICENSE
%global godocs          CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md RELEASING.md SECURITY.md testing.md\\\

Name:           %{goname}
Release:        %autorelease
Summary:        Google Cloud Client Libraries for Go

# Upstream license specification: BSD-3-Clause and Apache-2.0
License:        BSD-3-Clause AND Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|github.com/google/go-github/v35|github.com/google/go-github|' $(find . -iname '*.go' -type f)

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
# Disable tests requiring authentication
for test in "TestInstanceAdmin_GetCluster" \
            "TestInstanceAdmin_Clusters" \
            "TestInstanceAdmin_SetAutoscaling" \
            "TestInstanceAdmin_UpdateCluster_RemovingAutoscaling" \
            "TestInstanceAdmin_CreateInstance_WithAutoscaling" \
            "TestInstanceAdmin_CreateInstanceWithClusters_WithAutoscaling" \
            "TestInstanceAdmin_CreateCluster_WithAutoscaling" \
            "TestInstanceAdmin_UpdateInstanceWithClusters_IgnoresInvalidClusters" \
            "TestInstanceAdmin_UpdateInstanceWithClusters_WithAutoscaling" \
            "TestInstanceAdmin_UpdateInstanceAndSyncClusters_WithAutoscaling" \
            "TestCreateGetPutPatchListInstance" \
            "TestCreateGetRemoveSecurityPolicies" \
            "TestPaginationWithMaxRes" \
            "TestPaginationDefault" \
            "TestPaginationMapResponse" \
            "TestPaginationMapResponseMaxRes" \
            "TestCapitalLetter" \
            "TestInstanceGroupResize" \
            "TestIntegration" \
            "TestIntegration_GetGrafeasClient" \
            "TestParse" \
            "TestGoldens" \
            "TestClient_CustomRetry" \
            "TestCallBuilders" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
# get stuck for 10 mn
%gocheck -t storage
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
