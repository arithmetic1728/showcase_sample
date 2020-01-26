# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from libcst._position import CodePosition, CodeRange
from libcst.metadata.base_provider import (
    BaseMetadataProvider,
    BatchableMetadataProvider,
    ProviderT,
    VisitorMetadataProvider,
)
from libcst.metadata.expression_context_provider import (
    ExpressionContext,
    ExpressionContextProvider,
)
from libcst.metadata.full_repo_manager import FullRepoManager
from libcst.metadata.parent_node_provider import ParentNodeProvider
from libcst.metadata.position_provider import (
    PositionProvider,
    WhitespaceInclusivePositionProvider,
)
from libcst.metadata.reentrant_codegen import (
    CodegenPartial,
    ExperimentalReentrantCodegenProvider,
)
from libcst.metadata.scope_provider import (
    Access,
    Accesses,
    Assignment,
    Assignments,
    BaseAssignment,
    BuiltinAssignment,
    ClassScope,
    ComprehensionScope,
    FunctionScope,
    GlobalScope,
    QualifiedName,
    QualifiedNameProvider,
    QualifiedNameSource,
    Scope,
    ScopeProvider,
)
from libcst.metadata.type_inference_provider import TypeInferenceProvider
from libcst.metadata.wrapper import MetadataWrapper


__all__ = [
    "CodePosition",
    "CodeRange",
    "WhitespaceInclusivePositionProvider",
    "PositionProvider",
    "BaseMetadataProvider",
    "ExpressionContext",
    "ExpressionContextProvider",
    "BaseAssignment",
    "Assignment",
    "BuiltinAssignment",
    "Access",
    "Scope",
    "GlobalScope",
    "FunctionScope",
    "ClassScope",
    "ComprehensionScope",
    "ScopeProvider",
    "ParentNodeProvider",
    "QualifiedName",
    "QualifiedNameSource",
    "MetadataWrapper",
    "BatchableMetadataProvider",
    "VisitorMetadataProvider",
    "QualifiedNameProvider",
    "ProviderT",
    "Assignments",
    "Accesses",
    "TypeInferenceProvider",
    "FullRepoManager",
    # Experimental APIs:
    "ExperimentalReentrantCodegenProvider",
    "CodegenPartial",
]
