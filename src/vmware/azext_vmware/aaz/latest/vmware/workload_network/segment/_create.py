# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "vmware workload-network segment create",
)
class Create(AAZCommand):
    """Create a segment by id in a private cloud workload network.

    :example: Create a segment by ID in a workload network.
        az vmware workload-network segment create --resource-group group1 --private-cloud cloud1 --segment segment1 --display-name segment1 --connected-gateway /infra/tier-1s/gateway --revision 1 --dhcp-ranges 40.20.0.0 40.20.0.1 --gateway-address 40.20.20.20/16
    """

    _aaz_info = {
        "version": "2022-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.avs/privateclouds/{}/workloadnetworks/default/segments/{}", "2022-05-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.private_cloud = AAZStrArg(
            options=["-c", "--private-cloud"],
            help="Name of the private cloud",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.segment = AAZStrArg(
            options=["-n", "--name", "--segment"],
            help="NSX Segment identifier. Generally the same as the Segment's display name",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.connected_gateway = AAZStrArg(
            options=["--connected-gateway"],
            arg_group="Properties",
            help="Gateway which to connect segment to.",
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="Display name of the segment.",
        )
        _args_schema.revision = AAZIntArg(
            options=["--revision"],
            arg_group="Properties",
            help="NSX revision number.",
        )

        # define Arg Group "Subnet"

        _args_schema = cls._args_schema
        _args_schema.dhcp_ranges = AAZListArg(
            options=["--dhcp-ranges"],
            arg_group="Subnet",
            help="DHCP Range assigned for subnet.",
        )
        _args_schema.gateway_address = AAZStrArg(
            options=["--gateway-address"],
            arg_group="Subnet",
            help="Gateway address.",
        )

        dhcp_ranges = cls._args_schema.dhcp_ranges
        dhcp_ranges.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.WorkloadNetworksCreateSegments(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class WorkloadNetworksCreateSegments(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/workloadNetworks/default/segments/{segmentId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "segmentId", self.ctx.args.segment,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("connectedGateway", AAZStrType, ".connected_gateway")
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("revision", AAZIntType, ".revision")
                properties.set_prop("subnet", AAZObjectType)

            subnet = _builder.get(".properties.subnet")
            if subnet is not None:
                subnet.set_prop("dhcpRanges", AAZListType, ".dhcp_ranges")
                subnet.set_prop("gatewayAddress", AAZStrType, ".gateway_address")

            dhcp_ranges = _builder.get(".properties.subnet.dhcpRanges")
            if dhcp_ranges is not None:
                dhcp_ranges.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.connected_gateway = AAZStrType(
                serialized_name="connectedGateway",
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.port_vif = AAZListType(
                serialized_name="portVif",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.revision = AAZIntType()
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.subnet = AAZObjectType()

            port_vif = cls._schema_on_200_201.properties.port_vif
            port_vif.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.port_vif.Element
            _element.port_name = AAZStrType(
                serialized_name="portName",
            )

            subnet = cls._schema_on_200_201.properties.subnet
            subnet.dhcp_ranges = AAZListType(
                serialized_name="dhcpRanges",
            )
            subnet.gateway_address = AAZStrType(
                serialized_name="gatewayAddress",
            )

            dhcp_ranges = cls._schema_on_200_201.properties.subnet.dhcp_ranges
            dhcp_ranges.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
