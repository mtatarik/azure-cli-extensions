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
    "network firewall policy rule-collection-group list",
)
class List(AAZCommand):
    """List all Azure firewall policy rule collection groups.
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/firewallpolicies/{}/rulecollectiongroups", "2022-11-01"],
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
        _args_schema.policy_name = AAZStrArg(
            options=["--policy-name"],
            help="The name of the Firewall Policy.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FirewallPolicyRuleCollectionGroupsList(ctx=self.ctx)()
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

    class FirewallPolicyRuleCollectionGroupsList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleCollectionGroups",
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
                    "firewallPolicyName", self.ctx.args.policy_name,
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
                    "api-version", "2022-11-01",
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
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.priority = AAZIntType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rule_collections = AAZListType(
                serialized_name="ruleCollections",
            )

            rule_collections = cls._schema_on_200.value.Element.properties.rule_collections
            rule_collections.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.rule_collections.Element
            _element.name = AAZStrType()
            _element.priority = AAZIntType()
            _element.rule_collection_type = AAZStrType(
                serialized_name="ruleCollectionType",
                flags={"required": True},
            )

            disc_firewall_policy_filter_rule_collection = cls._schema_on_200.value.Element.properties.rule_collections.Element.discriminate_by("rule_collection_type", "FirewallPolicyFilterRuleCollection")
            disc_firewall_policy_filter_rule_collection.action = AAZObjectType()
            disc_firewall_policy_filter_rule_collection.rules = AAZListType()

            action = cls._schema_on_200.value.Element.properties.rule_collections.Element.discriminate_by("rule_collection_type", "FirewallPolicyFilterRuleCollection").action
            action.type = AAZStrType()

            rules = cls._schema_on_200.value.Element.properties.rule_collections.Element.discriminate_by("rule_collection_type", "FirewallPolicyFilterRuleCollection").rules
            rules.Element = AAZObjectType()
            _ListHelper._build_schema_firewall_policy_rule_read(rules.Element)

            disc_firewall_policy_nat_rule_collection = cls._schema_on_200.value.Element.properties.rule_collections.Element.discriminate_by("rule_collection_type", "FirewallPolicyNatRuleCollection")
            disc_firewall_policy_nat_rule_collection.action = AAZObjectType()
            disc_firewall_policy_nat_rule_collection.rules = AAZListType()

            action = cls._schema_on_200.value.Element.properties.rule_collections.Element.discriminate_by("rule_collection_type", "FirewallPolicyNatRuleCollection").action
            action.type = AAZStrType()

            rules = cls._schema_on_200.value.Element.properties.rule_collections.Element.discriminate_by("rule_collection_type", "FirewallPolicyNatRuleCollection").rules
            rules.Element = AAZObjectType()
            _ListHelper._build_schema_firewall_policy_rule_read(rules.Element)

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_firewall_policy_rule_read = None

    @classmethod
    def _build_schema_firewall_policy_rule_read(cls, _schema):
        if cls._schema_firewall_policy_rule_read is not None:
            _schema.description = cls._schema_firewall_policy_rule_read.description
            _schema.name = cls._schema_firewall_policy_rule_read.name
            _schema.rule_type = cls._schema_firewall_policy_rule_read.rule_type
            _schema.discriminate_by(
                "rule_type",
                "ApplicationRule",
                cls._schema_firewall_policy_rule_read.discriminate_by(
                    "rule_type",
                    "ApplicationRule",
                )
            )
            _schema.discriminate_by(
                "rule_type",
                "NatRule",
                cls._schema_firewall_policy_rule_read.discriminate_by(
                    "rule_type",
                    "NatRule",
                )
            )
            _schema.discriminate_by(
                "rule_type",
                "NetworkRule",
                cls._schema_firewall_policy_rule_read.discriminate_by(
                    "rule_type",
                    "NetworkRule",
                )
            )
            return

        cls._schema_firewall_policy_rule_read = _schema_firewall_policy_rule_read = AAZObjectType()

        firewall_policy_rule_read = _schema_firewall_policy_rule_read
        firewall_policy_rule_read.description = AAZStrType()
        firewall_policy_rule_read.name = AAZStrType()
        firewall_policy_rule_read.rule_type = AAZStrType(
            serialized_name="ruleType",
            flags={"required": True},
        )

        disc_application_rule = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule")
        disc_application_rule.destination_addresses = AAZListType(
            serialized_name="destinationAddresses",
        )
        disc_application_rule.fqdn_tags = AAZListType(
            serialized_name="fqdnTags",
        )
        disc_application_rule.http_headers_to_insert = AAZListType(
            serialized_name="httpHeadersToInsert",
        )
        disc_application_rule.protocols = AAZListType()
        disc_application_rule.source_addresses = AAZListType(
            serialized_name="sourceAddresses",
        )
        disc_application_rule.source_ip_groups = AAZListType(
            serialized_name="sourceIpGroups",
        )
        disc_application_rule.target_fqdns = AAZListType(
            serialized_name="targetFqdns",
        )
        disc_application_rule.target_urls = AAZListType(
            serialized_name="targetUrls",
        )
        disc_application_rule.terminate_tls = AAZBoolType(
            serialized_name="terminateTLS",
        )
        disc_application_rule.web_categories = AAZListType(
            serialized_name="webCategories",
        )

        destination_addresses = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").destination_addresses
        destination_addresses.Element = AAZStrType()

        fqdn_tags = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").fqdn_tags
        fqdn_tags.Element = AAZStrType()

        http_headers_to_insert = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").http_headers_to_insert
        http_headers_to_insert.Element = AAZObjectType()

        _element = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").http_headers_to_insert.Element
        _element.header_name = AAZStrType(
            serialized_name="headerName",
        )
        _element.header_value = AAZStrType(
            serialized_name="headerValue",
        )

        protocols = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").protocols
        protocols.Element = AAZObjectType()

        _element = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").protocols.Element
        _element.port = AAZIntType()
        _element.protocol_type = AAZStrType(
            serialized_name="protocolType",
        )

        source_addresses = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").source_addresses
        source_addresses.Element = AAZStrType()

        source_ip_groups = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").source_ip_groups
        source_ip_groups.Element = AAZStrType()

        target_fqdns = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").target_fqdns
        target_fqdns.Element = AAZStrType()

        target_urls = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").target_urls
        target_urls.Element = AAZStrType()

        web_categories = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "ApplicationRule").web_categories
        web_categories.Element = AAZStrType()

        disc_nat_rule = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NatRule")
        disc_nat_rule.destination_addresses = AAZListType(
            serialized_name="destinationAddresses",
        )
        disc_nat_rule.destination_ports = AAZListType(
            serialized_name="destinationPorts",
        )
        disc_nat_rule.ip_protocols = AAZListType(
            serialized_name="ipProtocols",
        )
        disc_nat_rule.source_addresses = AAZListType(
            serialized_name="sourceAddresses",
        )
        disc_nat_rule.source_ip_groups = AAZListType(
            serialized_name="sourceIpGroups",
        )
        disc_nat_rule.translated_address = AAZStrType(
            serialized_name="translatedAddress",
        )
        disc_nat_rule.translated_fqdn = AAZStrType(
            serialized_name="translatedFqdn",
        )
        disc_nat_rule.translated_port = AAZStrType(
            serialized_name="translatedPort",
        )

        destination_addresses = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NatRule").destination_addresses
        destination_addresses.Element = AAZStrType()

        destination_ports = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NatRule").destination_ports
        destination_ports.Element = AAZStrType()

        ip_protocols = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NatRule").ip_protocols
        ip_protocols.Element = AAZStrType()

        source_addresses = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NatRule").source_addresses
        source_addresses.Element = AAZStrType()

        source_ip_groups = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NatRule").source_ip_groups
        source_ip_groups.Element = AAZStrType()

        disc_network_rule = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NetworkRule")
        disc_network_rule.destination_addresses = AAZListType(
            serialized_name="destinationAddresses",
        )
        disc_network_rule.destination_fqdns = AAZListType(
            serialized_name="destinationFqdns",
        )
        disc_network_rule.destination_ip_groups = AAZListType(
            serialized_name="destinationIpGroups",
        )
        disc_network_rule.destination_ports = AAZListType(
            serialized_name="destinationPorts",
        )
        disc_network_rule.ip_protocols = AAZListType(
            serialized_name="ipProtocols",
        )
        disc_network_rule.source_addresses = AAZListType(
            serialized_name="sourceAddresses",
        )
        disc_network_rule.source_ip_groups = AAZListType(
            serialized_name="sourceIpGroups",
        )

        destination_addresses = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NetworkRule").destination_addresses
        destination_addresses.Element = AAZStrType()

        destination_fqdns = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NetworkRule").destination_fqdns
        destination_fqdns.Element = AAZStrType()

        destination_ip_groups = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NetworkRule").destination_ip_groups
        destination_ip_groups.Element = AAZStrType()

        destination_ports = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NetworkRule").destination_ports
        destination_ports.Element = AAZStrType()

        ip_protocols = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NetworkRule").ip_protocols
        ip_protocols.Element = AAZStrType()

        source_addresses = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NetworkRule").source_addresses
        source_addresses.Element = AAZStrType()

        source_ip_groups = _schema_firewall_policy_rule_read.discriminate_by("rule_type", "NetworkRule").source_ip_groups
        source_ip_groups.Element = AAZStrType()

        _schema.description = cls._schema_firewall_policy_rule_read.description
        _schema.name = cls._schema_firewall_policy_rule_read.name
        _schema.rule_type = cls._schema_firewall_policy_rule_read.rule_type
        _schema.discriminate_by(
                "rule_type",
                "ApplicationRule",
                cls._schema_firewall_policy_rule_read.discriminate_by(
                    "rule_type",
                    "ApplicationRule",
                )
            )
        _schema.discriminate_by(
                "rule_type",
                "NatRule",
                cls._schema_firewall_policy_rule_read.discriminate_by(
                    "rule_type",
                    "NatRule",
                )
            )
        _schema.discriminate_by(
                "rule_type",
                "NetworkRule",
                cls._schema_firewall_policy_rule_read.discriminate_by(
                    "rule_type",
                    "NetworkRule",
                )
            )


__all__ = ["List"]
