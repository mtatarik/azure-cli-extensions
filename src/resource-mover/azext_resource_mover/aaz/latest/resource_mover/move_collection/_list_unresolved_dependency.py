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
    "resource-mover move-collection list-unresolved-dependency",
)
class ListUnresolvedDependency(AAZCommand):
    """Lists a list of unresolved dependencies.

    The 'az resource-mover move-collection list-unresolved-dependency' command is applicable for 'RegionToRegion' type move collections. However, for move collections with move-type 'RegionToZone' dependencies are automatically added to the move collection once 'az resource-mover move-collection resolve-dependency' is executed. Please refer to 'az resource-mover move-collection resolve-dependency' command documentation for additional details.

    :example: List the unresolved dependencies.
        az resource-mover move-collection list-unresolved-dependency --move-collection-name MyMoveCollection --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2023-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.migrate/movecollections/{}/unresolveddependencies", "2023-08-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.move_collection_name = AAZStrArg(
            options=["-n", "--name", "--move-collection-name"],
            help="The Move Collection Name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of resource group. You can configure the default group using az configure --defaults group=<name>.",
            required=True,
        )
        _args_schema.dependency_level = AAZStrArg(
            options=["--dependency-level"],
            help="Defines the dependency level.",
            enum={"Descendant": "Descendant", "Direct": "Direct"},
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter to apply on the operation. For example, $apply=filter(count eq 2).",
        )
        _args_schema.orderby = AAZStrArg(
            options=["--orderby"],
            help="OData order by query option. For example, you can use $orderby=Count desc.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.UnresolvedDependenciesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class UnresolvedDependenciesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/moveCollections/{moveCollectionName}/unresolvedDependencies",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "moveCollectionName", self.ctx.args.move_collection_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$orderby", self.ctx.args.orderby,
                ),
                **self.serialize_query_param(
                    "dependencyLevel", self.ctx.args.dependency_level,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.summary_collection = AAZObjectType(
                serialized_name="summaryCollection",
            )
            _schema_on_200.total_count = AAZIntType(
                serialized_name="totalCount",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            summary_collection = cls._schema_on_200.summary_collection
            summary_collection.field_name = AAZStrType(
                serialized_name="fieldName",
            )
            summary_collection.summary = AAZListType()

            summary = cls._schema_on_200.summary_collection.summary
            summary.Element = AAZObjectType()

            _element = cls._schema_on_200.summary_collection.summary.Element
            _element.count = AAZIntType()
            _element.item = AAZStrType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.count = AAZIntType()
            _element.id = AAZStrType()

            return cls._schema_on_200


class _ListUnresolvedDependencyHelper:
    """Helper class for ListUnresolvedDependency"""


__all__ = ["ListUnresolvedDependency"]
