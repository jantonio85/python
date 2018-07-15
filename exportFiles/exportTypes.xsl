<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="1.0">
    <xsl:output method="xml" indent="yes"/>
    <xsl:param name="node"/>
    <!--xsl:param name="node">folders</xsl:param-->
    <xsl:template match="/">
        <repository>
          <valor-nodo>
            <xsl:value-of select="$node"/>
          </valor-nodo>
        <xsl:if test="/repository/repositoryInfo != ''">
            <xsl:copy-of select="/repository/repositoryInfo"/>
        </xsl:if>
        <xsl:if test="$node = 'folders'">
            <xsl:copy-of select="/repository/folders"/>
        </xsl:if>
        <xsl:if test="$node = 'thes'">
            <xsl:copy-of select="/repository/thesaurus"/>
        </xsl:if>
        <xsl:if test="$node = 'types'">
             <xsl:copy-of select="/repository/types"/>
        </xsl:if>
        </repository>
    </xsl:template>
</xsl:stylesheet>
