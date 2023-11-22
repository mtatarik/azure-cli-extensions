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
    "networkcloud baremetalmachine run-command",
    is_preview=True,
)
class RunCommand(AAZCommand):
    """Run the command or the script on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.

    :example: Run command on bare metal machine
        az networkcloud baremetalmachine run-command --bare-metal-machine-name "bareMetalMachineName" --arguments "--argument1" "argument2" --limit-time-seconds 60 --script "cHdkCg==" --resource-group "resourceGroupName"
    """

    _aaz_info = {
        "version": "2023-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/baremetalmachines/{}/runcommand", "2023-10-01-preview"],
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
        _args_schema.bare_metal_machine_name = AAZStrArg(
            options=["-n", "--name", "--bare-metal-machine-name"],
            help="The name of the bare metal machine.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9]{0,62}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "BareMetalMachineRunCommandParameters"

        _args_schema = cls._args_schema
        _args_schema.arguments = AAZListArg(
            options=["--arguments"],
            arg_group="BareMetalMachineRunCommandParameters",
            help="The list of string arguments that will be passed to the script in order as separate arguments.",
        )
        _args_schema.limit_time_seconds = AAZIntArg(
            options=["--limit-time-seconds"],
            arg_group="BareMetalMachineRunCommandParameters",
            help="The maximum time the script is allowed to run. If the execution time exceeds the maximum, the script will be stopped, any output produced until then will be captured, and the exit code matching a timeout will be returned (252).",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=14400,
                minimum=60,
            ),
        )
        _args_schema.script = AAZStrArg(
            options=["--script"],
            arg_group="BareMetalMachineRunCommandParameters",
            help="The base64 encoded script to execute on the bare metal machine.",
            required=True,
        )

        arguments = cls._args_schema.arguments
        arguments.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.BareMetalMachinesRunCommand(ctx=self.ctx)()
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

    class BareMetalMachinesRunCommand(AAZHttpOperation):
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
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [204]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_204,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/bareMetalMachines/{bareMetalMachineName}/runCommand",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "bareMetalMachineName", self.ctx.args.bare_metal_machine_name,
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
                    "api-version", "2023-10-01-preview",
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
            _builder.set_prop("arguments", AAZListType, ".arguments")
            _builder.set_prop("limitTimeSeconds", AAZIntType, ".limit_time_seconds", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("script", AAZStrType, ".script", typ_kwargs={"flags": {"required": True}})

            arguments = _builder.get(".arguments")
            if arguments is not None:
                arguments.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_204(self, session):
            pass

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
            _RunCommandHelper._build_schema_operation_status_result_read(cls._schema_on_200_201)

            return cls._schema_on_200_201


class _RunCommandHelper:
    """Helper class for RunCommand"""

    _schema_error_detail_read = None

    @classmethod
    def _build_schema_error_detail_read(cls, _schema):
        if cls._schema_error_detail_read is not None:
            _schema.additional_info = cls._schema_error_detail_read.additional_info
            _schema.code = cls._schema_error_detail_read.code
            _schema.details = cls._schema_error_detail_read.details
            _schema.message = cls._schema_error_detail_read.message
            _schema.target = cls._schema_error_detail_read.target
            return

        cls._schema_error_detail_read = _schema_error_detail_read = AAZObjectType()

        error_detail_read = _schema_error_detail_read
        error_detail_read.additional_info = AAZListType(
            serialized_name="additionalInfo",
            flags={"read_only": True},
        )
        error_detail_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_detail_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.target = AAZStrType(
            flags={"read_only": True},
        )

        additional_info = _schema_error_detail_read.additional_info
        additional_info.Element = AAZObjectType()

        _element = _schema_error_detail_read.additional_info.Element
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_detail_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_detail_read(details.Element)

        _schema.additional_info = cls._schema_error_detail_read.additional_info
        _schema.code = cls._schema_error_detail_read.code
        _schema.details = cls._schema_error_detail_read.details
        _schema.message = cls._schema_error_detail_read.message
        _schema.target = cls._schema_error_detail_read.target

    _schema_operation_status_result_read = None

    @classmethod
    def _build_schema_operation_status_result_read(cls, _schema):
        if cls._schema_operation_status_result_read is not None:
            _schema.end_time = cls._schema_operation_status_result_read.end_time
            _schema.error = cls._schema_operation_status_result_read.error
            _schema.id = cls._schema_operation_status_result_read.id
            _schema.name = cls._schema_operation_status_result_read.name
            _schema.operations = cls._schema_operation_status_result_read.operations
            _schema.percent_complete = cls._schema_operation_status_result_read.percent_complete
            _schema.resource_id = cls._schema_operation_status_result_read.resource_id
            _schema.start_time = cls._schema_operation_status_result_read.start_time
            _schema.status = cls._schema_operation_status_result_read.status
            return

        cls._schema_operation_status_result_read = _schema_operation_status_result_read = AAZObjectType()

        operation_status_result_read = _schema_operation_status_result_read
        operation_status_result_read.end_time = AAZStrType(
            serialized_name="endTime",
        )
        operation_status_result_read.error = AAZObjectType()
        cls._build_schema_error_detail_read(operation_status_result_read.error)
        operation_status_result_read.id = AAZStrType()
        operation_status_result_read.name = AAZStrType()
        operation_status_result_read.operations = AAZListType()
        operation_status_result_read.percent_complete = AAZFloatType(
            serialized_name="percentComplete",
        )
        operation_status_result_read.resource_id = AAZStrType(
            serialized_name="resourceId",
            flags={"read_only": True},
        )
        operation_status_result_read.start_time = AAZStrType(
            serialized_name="startTime",
        )
        operation_status_result_read.status = AAZStrType(
            flags={"required": True},
        )

        operations = _schema_operation_status_result_read.operations
        operations.Element = AAZObjectType()
        cls._build_schema_operation_status_result_read(operations.Element)

        _schema.end_time = cls._schema_operation_status_result_read.end_time
        _schema.error = cls._schema_operation_status_result_read.error
        _schema.id = cls._schema_operation_status_result_read.id
        _schema.name = cls._schema_operation_status_result_read.name
        _schema.operations = cls._schema_operation_status_result_read.operations
        _schema.percent_complete = cls._schema_operation_status_result_read.percent_complete
        _schema.resource_id = cls._schema_operation_status_result_read.resource_id
        _schema.start_time = cls._schema_operation_status_result_read.start_time
        _schema.status = cls._schema_operation_status_result_read.status


__all__ = ["RunCommand"]
